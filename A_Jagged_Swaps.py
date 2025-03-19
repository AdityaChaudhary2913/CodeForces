import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    arr = list(map(int, data[index:index+n]))
    index += n
    
    if arr[0] != 1:
        results.append("NO")
    else:
        results.append("YES")
        
sys.stdout.write("\n".join(results))