
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    counter = [0] * (n + 1)
    for x in arr:
        counter[x] += 1
    flg = 0
    for i in counter:
        if i == 1:
            flg = 1
            break
    if flg == 0:
        print(0)
        continue
    s = 0
    maxi = 0
    l = 0
    r = 0
    for e in range(n):
        if counter[arr[e]] > 1:
            s = e + 1
        else:
            if maxi < e - s + 1:
                maxi = e - s + 1
                l = s
                r = e   
    print(l+1, r+1)