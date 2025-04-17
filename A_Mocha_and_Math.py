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
    res = a[0]
    for i in range(1, n):
        res = res & a[i]
    
    results.append(str(res))

sys.stdout.write("\n".join(results))