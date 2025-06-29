console.log("Codeforces Voice Assistant: content.js loaded.");

const problemStatement = document.querySelector('.problem-statement');

if (problemStatement) {
  const questionText = problemStatement.innerText;

  const controls = document.createElement('div');
  controls.id = "cf-voice-assistant-controls";
  controls.innerHTML = `
    <button id="rewind-btn" title="Rewind 5s" disabled>⏪</button>
    <button id="play-pause-btn" title="Play">▶️</button>
    <button id="forward-btn" title="Forward 5s" disabled>⏩</button>
    <button id="restart-btn" title="Restart" disabled>🔄</button>
  `;
  problemStatement.prepend(controls);

  const playPauseBtn = document.getElementById('play-pause-btn');
  const rewindBtn = document.getElementById('rewind-btn');
  const forwardBtn = document.getElementById('forward-btn');
  const restartBtn = document.getElementById('restart-btn');

  playPauseBtn.addEventListener('click', () => {
    if (playPauseBtn.title === 'Play') {
      console.log("Sending 'speak' message");
      chrome.runtime.sendMessage({ action: 'speak', text: questionText });
    } else {
      console.log("Sending 'pause' message");
      chrome.runtime.sendMessage({ action: 'pause' });
    }
  });

  rewindBtn.addEventListener('click', () => {
    console.log("Sending 'rewind' message");
    chrome.runtime.sendMessage({ action: 'rewind' });
  });

  forwardBtn.addEventListener('click', () => {
    console.log("Sending 'forward' message");
    chrome.runtime.sendMessage({ action: 'forward' });
  });

  restartBtn.addEventListener('click', () => {
    console.log("Sending 'restart' message");
    chrome.runtime.sendMessage({ action: 'restart' });
  });

  // Listen for state updates from the background script
  chrome.runtime.onMessage.addListener((request) => {
    if (request.action === 'updateState') {
      console.log("Received state update:", request.state);
      switch (request.state) {
        case 'playing':
          playPauseBtn.textContent = '⏸️';
          playPauseBtn.title = 'Pause';
          rewindBtn.disabled = false;
          forwardBtn.disabled = false;
          restartBtn.disabled = false;
          break;
        case 'paused':
          playPauseBtn.textContent = '▶️';
          playPauseBtn.title = 'Play';
          rewindBtn.disabled = false;
          forwardBtn.disabled = false;
          restartBtn.disabled = false;
          break;
        case 'stopped':
          playPauseBtn.textContent = '▶️';
          playPauseBtn.title = 'Play';
          rewindBtn.disabled = true;
          forwardBtn.disabled = true;
          restartBtn.disabled = true;
          break;
      }
    }
  });
} else {
  console.error("Codeforces Voice Assistant: Could not find the '.problem-statement' element.");
}