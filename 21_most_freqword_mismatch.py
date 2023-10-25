from collections import defaultdict

def appr_pattern_match(pattern, text, d):
    # Initialize the pattern length.
    p_length = len(pattern)
    # Initializing the text length.
    t_length = len(text)
    # Storing the starting indices.
    count = 0
    # Iterating over the string.
    for i in range(t_length - p_length + 1):
        substring = text[i:i+p_length]
        mismatch = 0

        # Iterating over the substring.
        for j in range(p_length):
            if pattern[j] != substring[j]:
                mismatch += 1
            if mismatch > d:
                break
        if mismatch <= d:
            count += 1
    return count

def most_frq_mismatch(text, k, d):
    # Initializing the kmer Frequency dictionary.
    kmer_frq = defaultdict(int)
    # keeping track of the max count.
    max_count = 0

    # Iterating through the text and finding the pattern.
    for i in range(len(text) - k + 1):
        # Finding the pattern each time.
        pattern = text[i:i+k]
        # Finding the count.
        count = appr_pattern_match(pattern, text, d)
        # Updating the kmer pattern count each time.
        kmer_frq[pattern] = count
        max_count = max(max_count, count)

    # Returning only the pattern with the max count.
    freq_kmers = [pattern for pattern, counts in kmer_frq.items() if counts == max_count]

    return freq_kmers


with open('DNA_data.txt', 'r') as f1:
    lines = f1.read().split('\n')
text  = lines[0]
k, d = list(map(int, lines[1].split()))
for i in most_frq_mismatch(text, k, d):
    print(i, end = " ")