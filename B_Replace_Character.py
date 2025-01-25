from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    cnt = Counter(s)
    cnt = dict(sorted(cnt.items(), key=lambda item: item[1]))
    keys = list(cnt.keys())
    toBeReplaced = keys[-1]
    replacedOn = keys[0]
    print(s.replace(replacedOn, toBeReplaced, 1))