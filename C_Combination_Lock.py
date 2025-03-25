import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    if n % 2 == 0:
        results.append("-1")
    else:
        results.append(" ".join(str(i) for i in range(n, 0, -1)))

sys.stdout.write("\n".join(results))