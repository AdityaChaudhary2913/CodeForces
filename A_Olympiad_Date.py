import sys
from collections import Counter

input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

required_digits = [0, 0, 0, 1, 1, 2, 2, 3, 5]  # 3x 0, 1x 1, 2x 2, 1x 3, 1x 5

for _ in range(t):
    n = int(data[index])
    index += 1
    a = list(map(int, data[index:index + n]))
    index += n

    # Use Counter to track digit frequencies
    counter = Counter()
    found = False

    for i in range(n):
        counter[a[i]] += 1

        # Check if we have enough digits to form "01.03.2025"
        if (counter[0] >= 3 and counter[1] >= 1 and counter[2] >= 2 and
                counter[3] >= 1 and counter[5] >= 1):
            results.append(str(i + 1))  # We need i + 1 digits
            found = True
            break

    if not found:
        results.append("0")  # Impossible case

sys.stdout.write("\n".join(results) + "\n")
