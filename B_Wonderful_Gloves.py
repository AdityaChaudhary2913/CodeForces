import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    n = int(data[index])
    k = int(data[index + 1])
    index += 2
    left_gloves = list(map(int, data[index:index + n]))
    index += n
    right_gloves = list(map(int, data[index:index + n]))
    index += n
    ans = 0
    
    for i in range(n):
        ans += max(left_gloves[i], right_gloves[i])
    
    min_arr = []
    for i in range(n):
        min_arr.append(min(left_gloves[i], right_gloves[i]))
        
    min_arr.sort(reverse=True)
    # print(min_arr)
    for i in range(k-1):
        ans += min_arr[i]
    
    results.append(str(ans+1))

sys.stdout.write("\n".join(results))