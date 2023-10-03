def compute_frequency_array(Text, k):
    freq_array = [0] * (4 ** k)
    
    for i in range(len(Text) - k + 1): 
        kmer = Text[i:i+k]
        index = 0
        
        for j in range(k): 
            if kmer[j] == 'A':
                index = index * 4 + 0
            elif kmer[j] == 'C':
                index = index * 4 + 1
            elif kmer[j] == 'G':
                index = index * 4 + 2
            elif kmer[j] == 'T':
                index = index * 4 + 3
        
        freq_array[index] += 1  
    
    return freq_array 
Text = "ACGCGGCTCTGAAA"

k = 2
result = compute_frequency_array(Text, k)
print(result)
