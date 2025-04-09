import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

def get_number(n, x, y):
    if n == 1:
        if x == 1 and y == 1:
            return 1
        if x == 2 and y == 2:
            return 2
        if x == 2 and y == 1:
            return 3
        if x == 1 and y == 2:
            return 4
    
    oneWay = 2**(n-1)
    oneQuad = oneWay * oneWay
    
    if x <= oneWay and y <= oneWay:
        # Top-Left Quadrant
        return get_number(n-1, x, y)
    elif x <= oneWay and y > oneWay:
        # Top-Right Quadrant
        return 3 * oneQuad + get_number(n-1, x, y-oneWay)
    elif x > oneWay and y <= oneWay:
        # Bottom-Left Quadrant
        return 2 * oneQuad + get_number(n-1, x-oneWay, y)
    elif x > oneWay and y > oneWay:
        # Bottom-Right Quadrant
        return 1 * oneQuad + get_number(n-1, x-oneWay, y-oneWay)

def get_coord(n, d):
    if n == 1:
        if d == 1:
            return (1, 1)
        if d == 2:
            return (2, 2)
        if d == 3:
            return (2, 1)
        if d == 4:
            return (1, 2)
        
    oneWay = 2 ** (n - 1)
    oneQuad = oneWay * oneWay
    
    quadrant = (d - 1) // oneQuad
    offset = (d - 1) % oneQuad + 1
    
    sub_x, sub_y = get_coord(n - 1, offset)
    
    if quadrant == 0:
        # Top-left: no offset.
        return (sub_x, sub_y)
    elif quadrant == 1:
        # Bottom-right: add oneWay to both row and column.
        return (sub_x + oneWay, sub_y + oneWay)
    elif quadrant == 2:
        # Bottom-left: add oneWay to row.
        return (sub_x + oneWay, sub_y)
    elif quadrant == 3:
        # Top-right: add oneWay to column.
        return (sub_x, sub_y + oneWay)

for _ in range(t):
    n = int(data[index])
    index += 1
    q = int(data[index])
    index += 1
    for _ in range(q):
        op = data[index]
        index += 1
        if op == "->":
            x = int(data[index])
            y = int(data[index + 1])
            index += 2
            results.append(str(get_number(n, x, y)))
        elif op == "<-":
            d = int(data[index])
            index += 1
            x, y = get_coord(n, d)
            results.append(f"{x} {y}")

sys.stdout.write("\n".join(results))