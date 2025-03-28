import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    a = int(data[index])
    index += 1
    b = int(data[index])
    index += 1
    
    if a+b+1 < n or a==b and b==n:
        results.append("Yes")
    else:
        results.append("No")

sys.stdout.write("\n".join(results))