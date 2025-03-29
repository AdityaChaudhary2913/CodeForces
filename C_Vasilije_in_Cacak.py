import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    k = int(data[index])
    index += 1
    x = int(data[index])
    index += 1
    
    minSum = k*(k+1)
    maxSum = n*(n+1) - (n-k)*(n-k+1)
    
    if 2*x >= minSum and 2*x <= maxSum:
        results.append("YES")
    else:
        results.append("NO")

sys.stdout.write("\n".join(results))