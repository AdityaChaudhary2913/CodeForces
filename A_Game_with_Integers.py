import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    if n%3 == 0:
        results.append("Second")
    else:
        results.append("First")
sys.stdout.write("\n".join(results))