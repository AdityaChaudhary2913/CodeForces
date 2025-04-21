import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    s = list(data[index])
    index += 1
    
    firstIdx = -1
    for i in range(n):
        if s[i] == '1':
            firstIdx = i
            break
    
    secondIdx = -1
    for i in range(firstIdx+1, n-1):
        if s[i] == '0' and s[i+1] == '1':
            secondIdx = i
            break
    
    ops = 1
    
    if secondIdx == -1:
        lastZero = -1
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                lastZero = i
                break
        if firstIdx < lastZero:
            s[firstIdx:lastZero+1] = s[firstIdx:lastZero+1][::-1]
    elif firstIdx != -1 and secondIdx != -1:
        s = s[:firstIdx] + s[firstIdx:secondIdx+1][::-1] + s[secondIdx+1:]
    
    if s[0] == '1':
        ops += 1
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            ops += 1
        else:
            ops += 2
    results.append(str(ops))

sys.stdout.write("\n".join(results))
