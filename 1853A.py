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
    idx = 1
    mini = 100000000001
    for i in range(1, n):
        if a[i-1] > a[i]:
            results.append("0")
            flg = 1
            break
        elif mini > (a[i]-a[i-1]):
            mini = a[i]-a[i-1]
            idx = i-1
    if flg == 1:
        continue
    results.append(str((a[idx+1] - a[idx]) // 2 + 1))
            

sys.stdout.write("\n".join(results))