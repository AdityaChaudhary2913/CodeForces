
n = int(input())

teams = []

for i in range(n):
    home, away = map(int, input().split())
    teams.append([home, away])

count = 0

for i in range(n):
    for j in range(n):
        if teams[i][0] == teams[j][1]:
            count += 1

print(count)