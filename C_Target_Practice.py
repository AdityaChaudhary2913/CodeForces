
t = int(input())

for _ in range(t):
    arr = []
    for _ in range(10):
        arr.append(list(input().strip()))
    score = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 'X':
                if i == 0 or i == 9:
                    score += 1
                elif j == 0 or j == 9:
                    score += 1
                elif i == 1 or i == 8:
                    score += 2
                elif j == 1 or j == 8:
                    score += 2
                elif i == 2 or i == 7:
                    score += 3
                elif j == 2 or j == 7:
                    score += 3
                elif i == 3 or i == 6:
                    score += 4
                elif j == 3 or j == 6:
                    score += 4
                else:
                    score += 5
    print(score)
                    