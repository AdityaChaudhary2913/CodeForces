t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = [0] * n
    for i in range(1, n//k+1):
        arr[i*k - 1] = i
    maxi = max(arr)
    for i in range(n):
        if arr[i] == 0:
            arr[i] = maxi + 1
            maxi += 1
    for i in range(n):
        print(arr[i], end=' ')
    print()