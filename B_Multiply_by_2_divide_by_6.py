import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    cnt2, cnt3 = 0, 0
    while n % 2 == 0:
        n /= 2
        cnt2 += 1
    while n % 3 == 0:
        n /= 3
        cnt3 += 1
    if n == 1 and cnt2 <= cnt3:
        results.append(str(2*cnt3 - cnt2))
    else:
        results.append("-1")

sys.stdout.write("\n".join(results))