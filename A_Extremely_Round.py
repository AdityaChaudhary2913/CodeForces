import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    if n <= 10:
        results.append(str(n))
    elif n <= 100:
        results.append(str(9 + n//10))
    elif n <= 1000:
        results.append(str(18 + n//100))
    elif n <= 10000:
        results.append(str(27 + n//1000))
    elif n <= 100000:
        results.append(str(36 + n//10000))
    elif n < 1000000:
        results.append(str(45 + n//100000))

sys.stdout.write("\n".join(results))