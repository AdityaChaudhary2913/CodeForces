import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    a = list(data[index])
    index += 1
    ans = []
    maxi = n
    mini = 1
    for i in range(n-2, -1, -1):
        if a[i] == '<':
            ans.append(mini)
            mini += 1
        else:
            ans.append(maxi)
            maxi -= 1
    ans.append(mini)
    ans.reverse()
    results.append(" ".join(map(str, ans)))

sys.stdout.write("\n".join(results))