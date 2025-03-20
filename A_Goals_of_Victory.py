import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    a = list(map(int, data[index:index+(n-1)]))
    index += (n-1)
    count = sum(a)
    results.append(str(-count))

sys.stdout.write("\n".join(results))