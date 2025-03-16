import sys

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    if k == 1:
        print("YES" if arr == sorted(arr) else "NO")
    else:
        print("YES")
