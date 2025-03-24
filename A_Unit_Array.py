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
    negs = a.count(-1)
    poss = a.count(1)
    if negs > poss:
        ops = negs-poss
        if (negs - ops) % 2 == 0:
            results.append(str(negs-poss))
        else:
            results.append(str(negs-poss+1))
    else:
        if negs % 2 == 0:
            results.append("0")
        else:
            results.append("1")

sys.stdout.write("\n".join(results))