import sys, math
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
    a = list(map(int, data[index:index+(n*k)]))
    index += (n*k)
    incrementer = (n // 2) + 1
    a = a[::-1]
    ans = 0
    cnt = 0
    for i in range(incrementer-1, n*k, incrementer):
        ans += a[i]
        cnt += 1
        if cnt == k:
            break
    results.append(str(ans))

sys.stdout.write("\n".join(results))