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
    
    if n % 2 == 1:
        results.append("4")
        results.append("1 " + str(n-1))
        results.append("1 " + str(n-1))
        results.append(str(n-1) + " " + str(n))
        results.append(str(n-1) + " " + str(n))
    else:
        results.append("2")
        results.append("1 " + str(n))
        results.append("1 " + str(n))

sys.stdout.write("\n".join(results))