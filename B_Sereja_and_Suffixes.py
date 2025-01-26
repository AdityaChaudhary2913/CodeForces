
n, m = map(int, input().split())

arr = list(map(int, input().split()))

ans = [1] * n
unique = set()
unique.add(arr[n-1])

for i in range(n-2, -1, -1):
    if arr[i] not in unique:
        unique.add(arr[i])
        ans[i] = ans[i+1] + 1
    else:
        ans[i] = ans[i+1]

for i in range(m):
    l = int(input())
    print(ans[l-1])
    # print(len(set(arr[l-1:])))