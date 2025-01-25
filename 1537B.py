t = int(input())

for _ in range(t):
    n, m, i, j = map(int, input().split())
    y1 = 0
    y2 = 0
    y3 = 0
    y4 = 0
    if i <= (n+1)//2 and j <= (m+1)//2:
        y1, y2 = n, m
        y3, y4 = 1, 1
    elif i <= (n+1)//2:
        y1, y2 = n, 1
        y3, y4 = 1, m
    elif j <= (m+1)//2:
        y1, y2 = 1, m
        y3, y4 = n, 1
    else:
        y1, y2 = 1, 1
        y3, y4 = n, m
    print(y1, y2, y3, y4)