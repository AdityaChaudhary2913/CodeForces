t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    s = s.lower()
    for i in range(n-1):
        if s[i] == s[i+1]:
            s = s.replace(s[i], ' ', 1)
    s = s.replace(' ', '')
    if s == "meow":
        print("YES")
    else:
        print("NO")