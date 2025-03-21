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
    sorted(a)
    b = []
    c = []
    b.append(a[0])
    for i in range(1, n):
        if a[i] == 1:
            b.append(a[i])
        elif a[i] == a[i-1]:
            b.append(a[i])
            b.append(a[i-1])
        else:
            if a[i]%a[i-1] == 0:
                b.append(a[i])
            else:
                c.append(a[i])
    results.append(f"{len(b)} {len(c)}")
    results.append(" ".join(map(str, b)))
    results.append(" ".join(map(str, c)))

sys.stdout.write("\n".join(results))