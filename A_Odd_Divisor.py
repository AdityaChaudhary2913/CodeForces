import sys, math
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    flg = 0
    for i in range(50):
        n = n / 2
        if n == 1:
            results.append("NO")
            flg = 1
            break
    if flg == 0:
        results.append("YES")        

sys.stdout.write("\n".join(results))