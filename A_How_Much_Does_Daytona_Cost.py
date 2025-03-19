import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    k = int(data[index])
    index += 1
    arr = list(map(int, data[index:index+n]))
    index += n
    if k not in arr:
        results.append("NO")
    else:
        results.append("YES")
    # firstOccurrence = -1
    # lastOccurrence = -1
    # for i in range(n):
    #     if arr[i] == k:
    #         firstOccurrence = i
    #         break
    # for i in range(n-1, -1, -1):
    #     if arr[i] == k:
    #         lastOccurrence = i
    #         break
    # freq = {}
    # for i in range(firstOccurrence, lastOccurrence+1):
    #     try:
    #         freq[arr[i]] += 1
    #     except KeyError:
    #         freq[arr[i]] = 1
    # maxi = -1
    # totalOccurrence = freq[k]
    # flg = 0
    # for key, value in freq.items():
    #     if value > totalOccurrence: 
    #         results.append("NO")
    #         flg = 1
    #         break
    # if flg == 0:
    #     results.append("YES")

sys.stdout.write("\n".join(results))