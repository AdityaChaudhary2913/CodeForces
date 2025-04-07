import sys
from math import factorial
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

def ncr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

for _ in range(t):
    n = int(data[index])
    index += 1
    a = list(map(int, data[index:index+n]))
    index += n
    
    results.append(str(6 * ncr(10-n, 2)))

sys.stdout.write("\n".join(results))