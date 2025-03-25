import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    arr = list(map(int, data[index:index+n]))
    index += n
    maxi = 0
    lgst = 0 
    for i in range(len(arr)):
        if arr[i] == 0:
            lgst += 1
        else:
            if lgst > maxi:
                maxi = lgst
            lgst = 0
    results.append(str(max(maxi, lgst)))

sys.stdout.write("\n".join(results))