import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    x = int(data[index])
    index += 1
    y = int(data[index])
    index += 1
    n = int(data[index])
    index += 1
    
    k = n // x * x
    k += y
    
    if k > n:
        k -= x
        
    results.append(str(k))

sys.stdout.write("\n".join(results))