import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    m = int(data[index])
    index += 1
    k = int(data[index])
    index += 1
    arr = list(data[index])
    index += 1
    cnt = 0
    ops = 0
    for i in range(n):
        if arr[i] == '0':
            cnt += 1
            if cnt == m:
                for j in range(i, i+k):
                    if j >= n:
                        break
                    arr[j] = '1'
                ops += 1
                cnt = 0
        else:
            cnt = 0
    results.append(str(ops))

sys.stdout.write("\n".join(results))