def compute_frequency_array(Text, k):
    freq_array = [0] * (4 ** k)  # Step 1
    
    for i in range(len(Text) - k + 1):  # Step 2
        kmer = Text[i:i+k]
        index = 0
        
        for j in range(k):  # Step 3
            if kmer[j] == 'A':
                index = index * 4 + 0
            elif kmer[j] == 'C':
                index = index * 4 + 1
            elif kmer[j] == 'G':
                index = index * 4 + 2
            elif kmer[j] == 'T':
                index = index * 4 + 3
        
        freq_array[index] += 1  # Step 4
    
    return freq_array  # Step 5

# Example usage
Text = "ACGCGGCTCTGAAA"
k = 2
result = compute_frequency_array(Text, k)
print(result)
