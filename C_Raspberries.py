import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    k = int(data[index])
    index += 1
    a = list(map(int, data[index:index+n]))
    index += n
    ans = -1
    if k == 4:
        hasThree = False
        count = 0
        for i in a:
            if i % 4 == 0:
                ans = 0
                break
            elif i % 2 == 0:
                count += 1
            elif i % 4 == 3:
                hasThree = True
        if ans == -1:
            if count >= 2:
                ans = 0
            elif hasThree or count == 1:
                ans = 1
            else:
                ans = 2
        results.append(str(ans))
        continue
    flg = 0
    maxi = 0
    for v in a:
        if v % k == 0:
            results.append(str(0))
            flg = 1
            break
        else:
            maxi = max(maxi, v % k)
    if flg == 0:
        results.append(str(k-maxi))

sys.stdout.write("\n".join(results))