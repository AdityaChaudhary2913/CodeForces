import sys

data = sys.stdin.read().split()
t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = data[index]
    index += 1
    
    one = n.index("1")
    three = n.index("3")
    if one < three:
        results.append("13")
    else:
        results.append("31")
    
sys.stdout.write("\n".join(results))