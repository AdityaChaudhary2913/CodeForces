import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n, x = map(int, data[index:index+2])
    index += 2
    arr = set(map(int, data[index:index+n]))
    index += n
    ltrs = 0
    mini = 1
    for i in range(1, x+1):
        ltrs -= 1
        mini = min(mini, ltrs)
        if i in arr:
            ltrs = 0
    for i in range(x-1, -1, -1):
        ltrs -= 1
        mini = min(mini, ltrs)
        if i in arr:
            ltrs = 0
    results.append(str(-mini))

sys.stdout.write("\n".join(results))