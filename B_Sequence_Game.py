import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    b = list(map(int, data[index:index+n]))
    index += n
    arr = [b[0]]
    flg = 0
    for i in range(1, n):
        if b[i-1] <= b[i]:
            arr.append(b[i])
        else:
            flg = 1
            arr.append(b[i]-1 if (b[i]-1) > 0 else 1)
            arr.append(b[i])
    if flg == 0:
        results.append(str(len(b)))
        results.append(" ".join(map(str, b)))
        continue
    results.append(str(len(arr)))
    results.append(" ".join(map(str, arr)))

sys.stdout.write("\n".join(results))