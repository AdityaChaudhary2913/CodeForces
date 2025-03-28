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
    
    negs = a.count(-1)
    poss = n - negs
    
    ops = 0
    
    while poss<negs or negs%2:
        ops += 1
        poss += 1
        negs -= 1
    
    results.append(str(ops))

sys.stdout.write("\n".join(results))