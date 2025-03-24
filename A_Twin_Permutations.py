import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    a = list(map(int, data[index:index+n]))
    index += n
    b = []
    maxi = max(a) + 1
    for i in range(n):
        b.append(maxi-a[i])
    results.append(" ".join(map(str, b)))

sys.stdout.write("\n".join(results))