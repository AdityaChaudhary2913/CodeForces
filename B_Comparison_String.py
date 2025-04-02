import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    s = data[index]
    index += 1
    
    maxi = 1
    maxLen = 1
    for i in range(1, n):
        if s[i-1] == s[i]:
            maxi +=1 
        else:
            maxLen = max(maxLen, maxi)
            maxi = 1
    maxLen = max(maxLen, maxi)
    
    results.append(str(1+maxLen))

sys.stdout.write("\n".join(results))