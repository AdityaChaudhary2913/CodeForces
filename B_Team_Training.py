import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    x = int(data[index])
    index += 1
    a = list(map(int, data[index:index+n]))
    index += n
    
    a.sort(reverse=True)
    
    team_size = 0
    ans = 0
    
    for s in a:
        team_size += 1
        if team_size * s >= x:
            ans += 1
            team_size = 0

    results.append(str(ans))

sys.stdout.write("\n".join(results))