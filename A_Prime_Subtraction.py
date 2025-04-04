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
    
    if x-y > 1:
        results.append("YES")
    else:
        results.append("NO")
    

sys.stdout.write("\n".join(results))