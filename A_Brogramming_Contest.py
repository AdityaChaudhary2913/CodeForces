t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input().strip())
    t = []
    count = 0
    while '1' in s or '0' in t:
        for i in range(len(s)):
            if s[i] == '1':
                del_part =  s[i:]
                s = s[:i]
                t.extend(del_part)
                count += 1
                break
        for i in range(len(t)):
            if t[i] == '0':
                del_part =  t[i:]
                t = t[:i]
                s.extend(del_part)
                count += 1
                break
    print(count)