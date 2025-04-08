
# Cannot be accepted on codeforecs


import sys
from collections import Counter
data = sys.stdin.buffer.read().split()
t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    arr = list(map(int, data[index:index+n]))
    index += n

    freq = Counter(arr)

    max_freq = max(freq.values())

    if max_freq == n:
        results.append("0")
        continue

    ops = 0

    while max_freq * 2 <= n:
        ops += 1 + max_freq
        max_freq *=  2

    if max_freq < n:
        ops += 1 + (n - max_freq)

    results.append(str(ops))
sys.stdout.write("\n".join(results))