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
    count_ones = a.count(1)
    count_zeros = a.count(0)
    result = count_ones * (2 ** count_zeros)
    results.append(str(result))

sys.stdout.write("\n".join(results))