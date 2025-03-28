import sys
from collections import Counter
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
    a = map(str, data[index])
    index += 1
    
    freq = Counter(a)
    
    odds = 0
    
    for v in freq.values():
        if v % 2 == 1:
            odds += 1
    
    if odds <= k+1:
        results.append("YES")
    else:
        results.append("NO")
    

sys.stdout.write("\n".join(results))