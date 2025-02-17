t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    coin1 = 0
    for i in range(n):
        if arr[i] > 0:
            coin1 += arr[i]
    coin2 = 0
    for i in range(n-1, -1, -1):
        if arr[i] < 0:
            coin2 += abs(arr[i])
        
    s = 0
    coins = 0
    flg = 0
    while True:
        if arr[s] > 0:
            coins += arr[s]
            flg = 1
        else:
            coins += abs(arr[s])
            flg = -1
    
    print(max(coin1, coin2))
    