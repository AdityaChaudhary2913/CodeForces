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
    
    xor = 0
    for x in a:
        xor ^= x
    
    if xor == 0:
        results.append("0")
    else:
        if n % 2 == 1:
            results.append(str(xor))
        else:
            results.append("-1")

sys.stdout.write("\n".join(results))