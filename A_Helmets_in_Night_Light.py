import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    p = int(data[index])
    index += 1
    a = list(map(int, data[index:index+n]))
    index += n
    b = list(map(int, data[index:index+n]))
    index += n
    
    pair = [[a[i], b[i]] for i in range(n)]
    pair.append([n, p])
    pair.sort(key=lambda x: (x[1], -x[0]))
    idx = pair.index([n, p])
        
    tc, ip = 0, 0
    
    tc += p
    ip += 1
    
    for i in range(n+1):
        if ip == n:
            break
        if i == idx:
            tc += (n-ip)*pair[i][1]
            pair[i][0] -= (n-ip)
            ip += (n-ip)
        else:
            if pair[i][0] >= (n-ip):
                tc += (n-ip)*pair[i][1]
                pair[i][0] -= (n-ip)
                ip += (n-ip)
            else:
                tc += pair[i][0] * pair[i][1]
                ip += pair[i][0]
                pair[i][0] = 0
        
    results.append(str(tc))

sys.stdout.write("\n".join(results))