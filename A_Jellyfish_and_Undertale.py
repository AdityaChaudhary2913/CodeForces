import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    a = int(data[index])
    index += 1
    b = int(data[index])
    index += 1
    n = int(data[index])
    index += 1
    arr = list(map(int, data[index:index+n]))
    index += n
    
    secs = 0
    
    # arr.sort()
    
    for i in arr:
        if b == 0:
            break
        elif b == 1:
            b = min(1+i, a) - 1
            secs += 1
            continue
        elif (i+b) <= a:
            b += (i-1)
            secs += 1
            continue
        secs += (b-1)
        b = min(1+i, a) - 1
        secs += 1
    
    results.append(str(secs+b))
        

sys.stdout.write("\n".join(results))