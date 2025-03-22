
t = int(input())

for _ in range(t):
    n, k, x = map(int, input().split())

    if x != 1:
        print("YES")
        print(n)
        arr = [1] * n
        print(" ".join(map(str, arr)))
    else:
        if k == 1:
            print("NO")
        else:
            if n%k == 0:
                print("YES")
                print(int(n//k))
                arr = [k] * int(n//k)
                print(" ".join(map(str, arr)))
            elif n % 2 == 0:
                print("YES")
                print(int(n/2))
                arr = [2] * int(n/2)
                print(" ".join(map(str, arr)))
            else:
                if k >= 3:
                    print("YES")
                    print(int(n//2))
                    arr = [2] * (int(n//2)-1) + [3]
                    print(" ".join(map(str, arr)))
                else:
                    print("NO")
