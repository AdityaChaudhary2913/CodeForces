import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    x = int(data[index])
    index += 1
    k = int(data[index])
    index += 1
    if x % k != 0:
        results.append("1")
        results.append(f"{x}")
    else:
        results.append("2")
        results.append(f"{x-1} {1}")

sys.stdout.write("\n".join(results))