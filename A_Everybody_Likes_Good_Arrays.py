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
    
    b = [a[0]]
    
    ops = 0
    for i in range(1, n):
        if (a[i-1]%2 == 1 and a[i]%2 == 0) or (a[i-1]%2 == 0 and a[i]%2 == 1):
            b.append(a[i])
        else:
            mul = b[-1]
            b.pop()
            b.append(mul*a[i])
            ops += 1
    results.append(str(ops))

sys.stdout.write("\n".join(results))