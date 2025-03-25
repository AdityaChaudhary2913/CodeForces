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
    
    if k == 1 or (k == 3 and n != 1) or (k % 2 == 0 and n % 2 == 0) or (k % 2 == 1 and n % 2 == 1) or (k % 2 == 1 and n % 2 == 0):
        results.append("YES")
    
    elif k % 2 == 0 and n % 2 == 1:
        results.append("NO")
    

sys.stdout.write("\n".join(results))