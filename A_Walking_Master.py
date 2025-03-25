import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    arr = list(map(int, data[index:index+4]))
    index += 4
    
    if arr[2] <= arr[0] + arr[3]-arr[1] and arr[1] <= arr[3]:
        results.append(str(arr[3]-arr[1] + arr[3]-arr[1] - (arr[2]-arr[0])))
    else:
        results.append(str(-1))
sys.stdout.write("\n".join(results))