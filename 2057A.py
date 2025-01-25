t = int(input())
for i in range(t):
    row, col = map(int, input().split())
    print(max(row, col)+1)
