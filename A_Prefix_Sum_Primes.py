n = int(input())

arr = list(map(int, input().split()))

twos = arr.count(2)
ones = arr.count(1)

if twos == 0 or ones == 0:
    print(" ".join(map(str, arr)))
    
elif twos == 1:
    arr = [2] + [1] * ones
    print(" ".join(map(str, arr)))
    
else:
    arr = [2] + [1] + [2] * (twos - 1) + [1] * (ones - 1)
    print(" ".join(map(str, arr)))