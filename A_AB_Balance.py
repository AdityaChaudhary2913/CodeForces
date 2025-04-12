test = int(input())
for _ in range(1, test+1):
    string = input()
    n = len(string)
    
    if string[0] == string[-1]:
        print(string)
    
    else:
        print(string[-1] + string[1:])
                
        
        