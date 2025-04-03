import math

n = int(input())

flg = 0
for i in range(2, int(math.sqrt(n-2))+1):
    if (n-2)%i == 0:
        print("-1")
        flg = 1
        break

if flg == 0:
    print("2 " + str(n-2))