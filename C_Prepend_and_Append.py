import sys

input = sys.stdin.read
data = input().split()

t = int(data[0])  
index = 1
results = []

for _ in range(t):
    n = int(data[index])  
    index += 1
    a = data[index]  
    index += 1 
    
    s = 0
    e = n - 1

    while s <= e:
        if a[s] == a[e]:
            break
        s += 1
        e -= 1

    results.append(str(len(a[s:e+1]))) 
sys.stdout.write("\n".join(results) + "\n")
