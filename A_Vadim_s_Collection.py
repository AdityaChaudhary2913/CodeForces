import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    a = list(data[index])
    index += 1
    
    cnt = [0] * 10
    
    for i in range(10):
        cnt[int(a[i])] += 1
    
    result = []

    for i in range(10):
        threshold = 9-i
        for j in range(threshold, 10):
            if cnt[j] > 0:
                cnt[j] -= 1
                result.append(str(j))
                break 

    result = "".join(result)
    results.append(result)

sys.stdout.write("\n".join(results))