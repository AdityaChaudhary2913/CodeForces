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
    flg = 0
    for i in range(n):
        flg = 0
        for j in range(n):
            if i == j:
                continue
            elif abs(a[i] - a[j]) % k == 0:
                flg = 1
                break
        if flg == 0:
            results.append("YES")
            results.append(str(i+1))
            break
    if flg == 1:
        results.append("NO")

sys.stdout.write("\n".join(results))