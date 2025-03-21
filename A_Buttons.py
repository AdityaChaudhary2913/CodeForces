import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    a = list(map(int, data[index:index+3]))
    index += 3
    
    if a[0] == a[1]:
        if a[2]%2 == 0:
            results.append("Second")
        else:
            results.append("First")
        continue
    
    a[0] += (a[2] + 1) // 2  
    a[1] += a[2] // 2 
    
    if a[0] > a[1]:
        results.append("First")
    else:    
        results.append("Second")

sys.stdout.write("\n".join(results))