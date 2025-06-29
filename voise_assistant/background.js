console.log("Codeforces Voice Assistant: background.js loaded.");

let originalText = null;
let currentCharacter = 0;
let playbackState = 'stopped'; // Can be 'stopped', 'playing', or 'paused'

function updateContentScriptState(state) {
  playbackState = state;
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    if (tabs[0]) {
      chrome.tabs.sendMessage(tabs[0].id, { action: 'updateState', state: playbackState });
    }
  });
}

function onTtsEvent(event) {
  if (event.type === 'word') {
    currentCharacter = event.charIndex;
  } else if (event.type === 'end' || event.type === 'cancelled') {
    updateContentScriptState('stopped');
  } else if (event.type === 'error') {
    console.error("Speech synthesis error:", event.errorMessage);
    updateContentScriptState('stopped');
  }
}

function speak(text, startIndex = 0) {
  chrome.tts.stop(); // Stop current speech before starting new
  const textToSpeak = text.substring(startIndex);
  chrome.tts.speak(textToSpeak, { onEvent: onTtsEvent }, () => {
    if (chrome.runtime.lastError) {
      console.error("TTS speak error:", chrome.runtime.lastError.message);
      updateContentScriptState('stopped');
    } else {
      currentCharacter = startIndex;
      updateContentScriptState('playing');
    }
  });
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  console.log("Message received:", request.action, ", Current state:", playbackState);

  if (request.action === 'speak') {
    if (playbackState === 'stopped') {
      originalText = request.text;
      speak(originalText, 0);
    } else if (playbackState === 'paused') {
      chrome.tts.resume();
      updateContentScriptState('playing');
    }
  } else if (request.action === 'pause') {
    if (playbackState === 'playing') {
      chrome.tts.pause();
      updateContentScriptState('paused');
    }
  } else if (request.action === 'rewind') {
    if (originalText && playbackState !== 'stopped') {
      const newStart = Math.max(0, currentCharacter - 75);
      speak(originalText, newStart);
    }
  } else if (request.action === 'forward') {
    if (originalText && playbackState !== 'stopped') {
      const newStart = Math.min(originalText.length, currentCharacter + 75);
      speak(originalText, newStart);
    }
  } else if (request.action === 'restart') {
    if (originalText) {
      speak(originalText, 0);
    }
  }
});