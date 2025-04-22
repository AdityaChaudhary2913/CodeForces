test = int(input())

for _ in range(test):
    string = list(input())
    cnt0 = 0
    cnt1 = 0
    for i in range(len(string)):
        if string[i] == '0':
            cnt0 += 1
        else:
            cnt1 += 1
    t = ""
    j = -1
    for i in range(len(string)):
        if string[i] == '0' and cnt1 > 0:
            if string[j+1] == '1':
                continue
            t += '1'
            cnt1 -= 1
            j += 1
        elif string[i] == '1' and cnt0 > 0:
            if string[j+1] == '0':
                continue
            t += '0'
            cnt0 -= 1
            j += 1   
    print(len(string) - len(t))