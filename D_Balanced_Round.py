import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    k = int(data[index])
    index += 1
    a = list(map(int, data[index:index+n]))
    index += n
    a.sort()
    
    maxi = 1
    maxLen = 1
    for i in range(1, n):
        if abs(a[i]-a[i-1]) <= k:
            maxi += 1
        else:
            if maxi > maxLen:
                maxLen = maxi
            maxi = 1
    
    results.append(str(n-max(maxLen, maxi)))

sys.stdout.write("\n".join(results))