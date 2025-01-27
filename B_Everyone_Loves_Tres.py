t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1 or n == 3:
        print("-1")
    elif n % 2 == 0:
        for i in range(n-2):
            print("3", end="")
        print("66")
    else:
        for i in range(n-4):
            print("3", end="")
        print("6366")