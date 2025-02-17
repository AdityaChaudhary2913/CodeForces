t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        if arr[i] <= max(i, n-i-1)*2:
            print("NO")
            break
    else:
        print("YES")