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
    
    for i in range(n):
        if a[i] == 1:
            a[i] += 1
    for i in range(n):
        if a[i] % a[i-1] == 0:
            a[i] += 1
    
    results.append(" ".join(map(str, a)))

sys.stdout.write("\n".join(results))