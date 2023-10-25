from collections import defaultdict

# Finding the hamming distance between the two strings.
def hamming_distance(string1, string2):
    count = 0
    for char1, char2 in zip(string1, string2):
        if char1 != char2:
            count += 1
        else: pass
    return count

# Generating neighbors.
def generate_neighbors(pattern, d):
    # Checking the Edge case conditions.
    if d == 0: return [pattern]
    elif len(pattern) == 1: return ['A', 'C', 'G', 'T']
    else: pass

    # Initializing a set to keep track of the neighbors.
    neighbors = set()
    # Generating the suffix of the neighbours.
    s_n = generate_neighbors(pattern[1:], d)
    # Interating throught the suffix.
    for suffix in s_n:
        # Checking if the hamming distance of both is less than d.
        if hamming_distance(pattern[1:], suffix) < d:
            # Iterating through the nucleotides.
            for n in ['A', 'C', 'G', 'T']:
                neighbors.add(n + suffix)
        else: neighbors.add(pattern[0] + suffix)
    return list(neighbors)
  
def freq_pattern_mismatch(text, k, d):
    # Intializing the kmer frequencies dictionary.
    kmer_frq = defaultdict(int)
    # Initializing a variable to keep track of the maximum count.
    max_c = 0
    # Iterating through kmer.
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        # Finding the neighbors of the kmer.
        neighbors = generate_neighbors(kmer, d)
        # Iterating through the neighbors to find the mismatch count.
        for pattern in neighbors:
            kmer_frq[pattern] += 1
            max_c = max(max_c, kmer_frq[pattern])

    # Returning the maximum count pattern from the kmer frequencies dictionary
    result = [pattern for pattern, count in kmer_frq.items() if count == max_c]
    return result

with open('DNA_data.txt', 'r') as f1:
    lines = f1.read().split('\n')
text  = lines[0]
k, d = list(map(int, lines[1].split()))
for i in freq_pattern_mismatch(text, k, d):
    print(i, end = " ")