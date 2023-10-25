from collections import defaultdict

def count_with_mismatches(pattern, text, d):
    pattern_length = len(pattern)
    text_length = len(text)
    count = 0

    for i in range(text_length - pattern_length + 1):
        substring = text[i:i+pattern_length]
        mismatches = 0

        for j in range(pattern_length):
            if pattern[j] != substring[j]:
                mismatches += 1

            if mismatches > d:
                break

        if mismatches <= d:
            count += 1

    return count

def frequent_words_with_mismatches(text, k, d):
    kmer_counts = defaultdict(int)
    max_count = 0
    frequent_kmers = []

    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        counts = count_with_mismatches(pattern, text, d)
        kmer_counts[pattern] = counts
        max_count = max(max_count, counts)

    for pattern, counts in kmer_counts.items():
        if counts == max_count:
            frequent_kmers.append(pattern)

    return frequent_kmers

# Example usage
text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1

result = frequent_words_with_mismatches(text, k, d)
print(result)
