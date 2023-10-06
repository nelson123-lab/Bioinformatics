# Finding the count of each kmer within the DNA_string
def Pattern_count(DNA_string, Pattern):
    # Finding the count each time and returning it since it runs within a for loop.
    Count = sum(1 for i in range(len(DNA_string) - len(Pattern) + 1) if DNA_string[i:i+len(Pattern)] == Pattern)
    return Count

# Finding all possible combinations of DNA base with length = k
def Generate_kmer(k):
    bases = ['A', 'C', 'G', 'T']
    # Making a copy of the DNA bases.
    DNA_bases = bases
    # Generating combinations of DNA base, this can also be done using itertools.product().
    for _ in range(k - 1):
        DNA_bases = [i+j for i in DNA_bases for j in bases]
    return DNA_bases
   
with open('DNA_data.txt', 'r') as f1:
    lines = f1.read().split('\n')
# Loading the DNA string and k values.
DNA_string, k  = lines[0], int(lines[1])
# Generating the kmers.
kmer = Generate_kmer(k)
with open("Output_dataset.txt", "w") as file:
    for pattern in kmer:
        count = Pattern_count(DNA_string, pattern)
        file.write(str(count) + " ")