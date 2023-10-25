def rev_comp(pattern):
    # Initializing the reverse nucleotide sequence.
    comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    # Creating an empty string to store the reverse nucleotide sequence.
    output = ''
    # Iterating over the patterns.
    for nucleotide in pattern[::-1]:
        output += comp[nucleotide]
    return output

with open('DNA_data.txt', 'r') as f1:
    lines = f1.read().split('\n')
print(rev_comp(lines[0]))