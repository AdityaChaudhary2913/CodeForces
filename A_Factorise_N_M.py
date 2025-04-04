import sys
data = sys.stdin.read().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    
    if n == 2:
        results.append("2")
        continue
    results.append("3")
sys.stdout.write("\n".join(results))