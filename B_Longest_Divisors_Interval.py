import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    
    for i in range(1, 101):
        if n%i == 0 and n%(i+1) != 0:
            results.append(str(i))
            break

sys.stdout.write("\n".join(results))