import sys
input = sys.stdin.read

def solve():
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    result = []
    
    for _ in range(t):
        n, m, k = map(int, data[index:index+3])
        index += 3
        ans = 0
        half = (n * m) // 2
        
        if m % 2 == 1:
            half = (n * (m + 1)) // 2
        
        if k <= half:
            ans = 1
        else:
            rem = k - half
            q = rem // n
            r = rem % n
            
            if r == 0:
                if m % 2 == 0:
                    ans = 2 * q
                else:
                    ans += 2 * q
            else:
                q += 1
                if m % 2 == 0:
                    ans = 2 * q
                else:
                    ans += 2 * q
        
        result.append(str(ans))
    
    sys.stdout.write("\n".join(result) + "\n")

solve()