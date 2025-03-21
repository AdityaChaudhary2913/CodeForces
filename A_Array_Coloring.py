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
    
    even = 0
    odd = 0
    for i in a:
        if i % 2 == 0:
            even = 1
        else:
            odd += 1
    if odd % 2 == 0:
        results.append("YES")
    else:
        results.append("NO")
            

sys.stdout.write("\n".join(results))