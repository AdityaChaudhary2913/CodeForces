
n = int(input())

mini = 100001

arr = list(map(int, input().split()))

for i in range(n):
    mini = min(mini, abs(arr[i]))
    
print(mini)