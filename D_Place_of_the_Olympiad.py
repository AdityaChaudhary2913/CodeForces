import sys

def solve():
    n, m, k = map(int, sys.stdin.readline().split())
    l, r = 0, m

    while l + 1 < r:
        mid = (l + r) // 2
        if (m // (mid + 1) * mid + m % (mid + 1)) * n >= k:
            r = mid
        else:
            l = mid

    print(r)

def main():
    t = int(sys.stdin.readline().strip()) 
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
