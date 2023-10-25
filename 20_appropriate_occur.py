def appr_pattern_match(pattern, text, d):
    # Initialize the pattern length.
    p_length = len(pattern)
    # Initializing the text length.
    t_length = len(text)
    # Storing the starting indices.
    indices = []
    d = int(d)

    # Iterating over the string.
    for i in range(t_length - p_length + 1):
        substring = text[i:i+p_length]
        count = 0

        # Iterating over the substring.
        for j in range(p_length):
            if pattern[j] != substring[j]:
                count += 1
            if count > d:
                break
        if count <= d:
            indices.append(i)
    return indices

with open('DNA_data.txt', 'r') as f1:
    lines = f1.read().split('\n')
pattern, text, d  = lines[0], lines[1], lines[2]
for i in appr_pattern_match(pattern, text, d):
    print(i, end = " ")