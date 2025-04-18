import sys, math
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    a = int(data[index])
    index += 1
    b = int(data[index])
    index += 1
    results.append(str((a*b)//(math.gcd(a, b))))

sys.stdout.write("\n".join(results))