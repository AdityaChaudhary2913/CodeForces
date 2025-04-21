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
    a = list(map(int, data[index:index+n]))
    index += n
    a = Counter(a)
    results.append(str(len(a)))

sys.stdout.write("\n".join(results))