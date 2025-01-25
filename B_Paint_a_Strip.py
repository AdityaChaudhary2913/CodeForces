t = int(input())
for _ in range(t):
    n = int(input())
    ans = 1
    curr = 1
    while True:
        if curr >= n:
            print(ans)
            break
        ans += 1
        curr = curr*2 + 2