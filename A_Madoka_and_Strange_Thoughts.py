import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    
    results.append(str(n + n//2 * 2 + n//3 *2))

sys.stdout.write("\n".join(results))