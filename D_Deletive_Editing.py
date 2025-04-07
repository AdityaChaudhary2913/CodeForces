def solve():
    import sys
    input_data = sys.stdin.read().split()
    t = int(input_data[0])
    index = 1
    results = []
    
    for _ in range(t):
        s = list(input_data[index])  # Convert string to list for in-place modifications
        index += 1
        t_str = input_data[index]
        index += 1

        n = len(s)
        
        # Create a frequency list for t (for 26 uppercase letters)
        frequency_in_t = [0] * 26
        for char in t_str:
            frequency_in_t[ord(char) - ord('A')] += 1
        
        # Process s in reverse order
        for i in range(n - 1, -1, -1):
            pos = ord(s[i]) - ord('A')
            if frequency_in_t[pos] > 0:
                frequency_in_t[pos] -= 1  # Use one occurrence
            else:
                s[i] = ''  # Mark for deletion
        
        # Build the final string from characters that are not marked for deletion
        final_string = ''.join(s)
        
        # Compare the final string with t_str
        results.append("YES" if final_string == t_str else "NO")
    
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    solve()
