import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n, m, i, j = list(map(int, data[index:index+4]))
    index += 4
    if i == 1 and j == 1:
        results.append(f"{n} {m} {n} {m}")
    elif n == i and m == j:
        results.append("1 1 1 1")
    elif i == 1 and m == j:
        results.append(f"{n} 1 {n} 1")
    elif n == i and j == 1:
        results.append(f"1 {m} 1 {m}")
    else:
        results.append(f"1 1 {n} {m}")
sys.stdout.write("\n".join(results))