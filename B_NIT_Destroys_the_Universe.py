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
    
    if all(x == 0 for x in a):
        results.append("0")
        continue
    
    if 0 not in a:
        results.append("1")
        continue

    if a.count(0) == 1:
        if a[0] == 0 or a[-1] == 0:
            results.append("1")
        else:
            results.append("2")
        continue
    
    first = -1
    for i in range(n):
        if a[i] != 0:
            first = i
            break

    last = -1
    for i in range(n-1, -1, -1):
        if a[i] != 0:
            last = i
            break
        
    if 0 not in a[first:last+1]:
        results.append("1")
        continue
    
    results.append(str(2))

sys.stdout.write("\n".join(results))