t = int(input())

for _ in range(t):
    n = int(input())
    freq = {}
    arr = list(map(int, input().split())) 

    for a in arr:
        freq[a] = freq.get(a, 0) + 1  # Using .get() to avoid KeyError
        
    if len(freq) == 1:
        print("Yes")

    elif len(freq) > 2:
        print("No")
    
    else:
        v1, v2 = list(freq.values())
        if abs(v1 - v2) <= 1:
            print("Yes")
        else:
            print("No")