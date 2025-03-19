import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    m = int(data[index])
    index += 1
    x = data[index]
    index += 1
    s = data[index]
    index += 1
    
    if s in x:
        results.append("0")
    else:
        i = 1
        while True:
            x += x
            if s in x:
                results.append(f"{i}")
                break
            i += 1
            if i > 5:
                results.append("-1")
                break

sys.stdout.write("\n".join(results))