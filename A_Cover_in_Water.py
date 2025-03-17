import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    arr = data[index]
    index += 1
    if "." not in arr:
        results.append(str(0))
    elif "..." in arr:
        results.append(str(2))
    else:
        # More optimized than manual loop counting
        cnt = arr.count(".")
        results.append(str(cnt))

sys.stdout.write("\n".join(results))