test = int(input())

for _ in range(test):
    a, b = list(map(int, input().split()))
    
    if a == b:
        print("0 0")
        continue
    g = abs(a - b)
    mini = min(a % g, g - a % g)
    print(f"{g} {mini}")