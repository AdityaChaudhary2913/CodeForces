import math

test = int(input())

for _ in range(test):
    n = int(input())
    
    if n%2 == 1 or n < 4:
        print("-1")
    else:
        maxi = n // 4
        mini = (n + 5) // 6
        print(str(mini) + " " + str(maxi))