import sys
data = sys.stdin.read().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    
    arr = list(map(int, data[index:index+n]))
    index += n
    
    ans = max(arr[-1]-min(arr), max(arr)-arr[0])
    
    for i in range(1, n):
        ans = max(ans, arr[i-1]-arr[i])
        
    results.append(str(ans))
    
sys.stdout.write("\n".join(results))