import sys
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
    for i in range(1, n-1):
        if a[i-1] < a[i] > a[i+1] :
            results.append("YES")
            results.append(f"{i} {i+1} {i+2}")
            flg = 1
            break
    if flg == 0:
        results.append("NO")
sys.stdout.write("\n".join(results))