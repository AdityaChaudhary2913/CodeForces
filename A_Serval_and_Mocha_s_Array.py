import sys, math
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

    if 1 in a:
        results.append("Yes")
        continue

    else:
        flg = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                elif math.gcd(a[i], a[j]) <= 2:
                    results.append("Yes")
                    flg = 1
                    break
            if flg == 1:
                break
        if flg == 0:
            results.append("No")

sys.stdout.write("\n".join(results))