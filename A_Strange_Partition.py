import sys, math
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    x = int(data[index])
    index += 1
    a = list(map(int, data[index:index+n]))
    index += n
    total = sum(a)
    mini = (total + x - 1) // x
    maxi = 0
    for i in range(n):
        maxi += math.ceil(a[i] / x)
    results.append(f"{mini} {maxi}")

sys.stdout.write("\n".join(results))