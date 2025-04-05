n = int(input())
m = int(input())

def power(b):
    if b == 0:
        return 1
    if b == 1:
        return 2
    x = power(int(b//2))
    ans = 0
    if b % 2 == 1:
        ans = x * x * 2
    else:
        ans = x * x
    return ans

mod = power(n)

print(str(m % mod))