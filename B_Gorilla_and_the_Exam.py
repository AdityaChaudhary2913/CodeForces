from collections import Counter

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    digitCount = Counter(arr)
    ans = len(digitCount)
    if k == 0:
        print(ans)
        continue
    freq = list(digitCount.values())
    freq.sort()
    for val in freq:
        k -= val
        if k<0:
            break
        ans -= 1
    print(max(ans, 1))