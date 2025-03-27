import sys

input = sys.stdin.read
data = input().split()

t = int(data[0])  
index = 1
results = []

for _ in range(t):
    moves = list(map(int, data[index:index+2]))
    index += 2
    king = list(map(int, data[index:index+2]))
    index += 2
    queen = list(map(int, data[index:index+2]))
    index += 2

    # King points
    k1 = (king[0] - moves[0], king[1] - moves[1])
    k2 = (king[0] + moves[0], king[1] - moves[1])
    k3 = (king[0] - moves[0], king[1] + moves[1])
    k4 = (king[0] + moves[0], king[1] + moves[1])
    k5 = (king[0] - moves[1], king[1] - moves[0])
    k6 = (king[0] + moves[1], king[1] - moves[0])
    k7 = (king[0] - moves[1], king[1] + moves[0])
    k8 = (king[0] + moves[1], king[1] + moves[0])

    # Queen points
    q1 = (queen[0] - moves[0], queen[1] - moves[1])
    q2 = (queen[0] + moves[0], queen[1] - moves[1])
    q3 = (queen[0] - moves[0], queen[1] + moves[1])
    q4 = (queen[0] + moves[0], queen[1] + moves[1])
    q5 = (queen[0] - moves[1], queen[1] - moves[0])
    q6 = (queen[0] + moves[1], queen[1] - moves[0])
    q7 = (queen[0] - moves[1], queen[1] + moves[0])
    q8 = (queen[0] + moves[1], queen[1] + moves[0])

    # Convert lists to sets of tuples
    k = {k1, k2, k3, k4, k5, k6, k7, k8}
    q = {q1, q2, q3, q4, q5, q6, q7, q8}

    results.append(str(len(k & q)))

sys.stdout.write("\n".join(results) + "\n")
