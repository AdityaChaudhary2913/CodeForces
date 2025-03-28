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
    
    if a[0] == a[-1]:
        results.append("NO")

    else:
        results.append("YES")
        results.append(str(a[-1]) + " " + " ".join(map(str, a[:n-1])))

sys.stdout.write("\n".join(results))