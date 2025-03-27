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

    flg = 0
    for i in range(n-1):
        if a[:i+1].count(2) == a[i+1:].count(2):
            results.append(f"{i+1}")
            flg = 1
            break
    if flg == 0:
        results.append("-1")

sys.stdout.write("\n".join(results))