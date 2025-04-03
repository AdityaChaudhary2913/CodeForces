import sys, math
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
    
    arr = []
    for i in range(n):
        arr.append(abs(a[i]-1-i))
        
    gcd = 0
    for i in range(1, n):
        gcd = math.gcd(gcd, arr[i])
    results.append(str(gcd))

sys.stdout.write("\n".join(results))