import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    q = int(data[index])
    index += 1
    arr = list(map(int, data[index:index+n]))
    index += n
    initSum = sum(arr)
    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + arr[i - 1]
    for i in range(q):
        l = int(data[index])
        index += 1
        r = int(data[index])
        index += 1
        k = int(data[index])
        index += 1
        
        addSum = k*(r-l+1)
        subSum = pref[r] - pref[l-1]
        
        if (initSum + addSum - subSum) % 2 == 1:
            results.append("YES")
        else:
            results.append("NO")

sys.stdout.write("\n".join(results))