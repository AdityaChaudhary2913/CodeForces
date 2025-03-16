import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

for _ in range(t):
    n, k = map(int, data[index:index+2])
    index += 2
    arr = list(map(int, data[index:index+n]))
    index += n
    if k == 1:
        if arr == sorted(arr):
            print("YES")
        else:
            print("NO")
    else:
        print("YES")