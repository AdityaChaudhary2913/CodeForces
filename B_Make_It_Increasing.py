import math

test = int(input())

for _ in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    
    flg = 0
    for i in range(n-1, -1, -1):
        if arr[i] < i:
            print("-1")
            flg = 1
            break
    if flg == 1:
        continue
    
    ops = 0
    
    for i in range(n-2, -1, -1):
        if arr[i] < arr[i+1]:
            continue
        
        if arr[i+1] == 0:
            ops = -1
            break
        
        k = int(math.floor(math.log2(arr[i] / arr[i+1]))) + 1
        
        ops += k
        
        arr[i] = arr[i] // (2**k)
            
    print(ops)
    