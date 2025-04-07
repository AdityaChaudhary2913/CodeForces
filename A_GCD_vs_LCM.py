import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    
    results.append("1 " + str(n-3) + " 1 1")

sys.stdout.write("\n".join(results))