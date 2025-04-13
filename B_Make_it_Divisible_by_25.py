
def min_moves_for_candidate(s, candidate):
    n = len(s)
    
    moves = 0
    pos_second = -1
    for i in range(n - 1, -1, -1):
        if s[i] == candidate[1]:
            pos_second = i
            break
        else:
            moves += 1
    if pos_second == -1:
        return 100

    moves_second = 0
    pos_first = -1
    for j in range(pos_second - 1, -1, -1):
        if s[j] == candidate[0]:
            pos_first = j
            break
        else:
            moves_second += 1
    if pos_first == -1:
        return 100
    
    return moves + moves_second

def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    
    t = int(input_data[0])
    results = []
    index = 1
    valid_candidates = ["00", "25", "50", "75"]
    
    for _ in range(t):
        s = input_data[index]
        index += 1
        min_moves = 100
        
        for candidate in valid_candidates:
            moves = min_moves_for_candidate(s, candidate)
            min_moves = min(min_moves, moves)
        
        results.append(str(min_moves))
    
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    solve()
