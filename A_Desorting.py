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
    mini = 10000000001
    for i in range(1, len(a)):
        mini = min(mini, a[i]-a[i-1])
        if a[i-1] > a[i]:
            results.append("0")
            flg = 1
            break
    if flg == 1:
        continue
    results.append(str(mini))
    

sys.stdout.write("\n".join(results))