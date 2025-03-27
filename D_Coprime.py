import sys, math
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    a = list(map(int, data[index:index+n]))
    index += n

    dct = {}
    for i in range(n-1, -1, -1):
        if a[i] not in dct:
            dct[a[i]] = i+1
    
    ans = -1
    for x in a:
        for y in a:
            if math.gcd(x, y) == 1:
                ans = max(ans, dct[x] + dct[y])
    
    results.append(str(ans))

sys.stdout.write("\n".join(results))