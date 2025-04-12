test = int(input())

for _ in range(test):
    x, n = list(map(int, input().split()))
    
    ans = 0
    
    if n%4 == 0:
        ans = 0
    elif n%4 == 1:
        ans = -n
    elif n%4 == 2:
        ans = 1
    elif n%4 == 3:
        ans = n + 1
        
    if x % 2 == 0:
        print(str(ans+x))
    else:
        print(str(-ans+x))