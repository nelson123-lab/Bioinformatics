# Function for finding the Hamming Distance.
def HammingDistance(string1, string2):
    count = 0
    for char1, char2 in zip(string1, string2):
        if char1 != char2:
            count += 1
        else: pass
    return count

# Function to find the d neighborhood.
def d_neighbors(pattern, d):
    # Defining the nucleotices of the neighbors.
    nucleotides = ['A', 'C', 'G', 'T']
    # Defining a set for the neighbors list.
    dNeighbors = set()
    # Returing the pattern itself.
    if d == 0: return {pattern}  
    # Returning all nucleotides if length of pattern is 1.
    elif len(pattern) == 1: return set(nucleotides)  
    else: pass
    # Recursively finding the d neighbors of the suffix.
    suffix = d_neighbors(pattern[1:], d)  
    # Checking if the Hamming distance is less than d to find all the kmer.
    for text in suffix:
        if HammingDistance(pattern[1:], text) < d: 
            # Adding all possible nucleotide combinations to the neighbors set. 
            for nucleotide in nucleotides:
                dNeighbors.add(nucleotide + text)
        else:
            dNeighbors.add(pattern[0] + text)  
    return dNeighbors

pattern = "AGCAACGCAC"
d = 3
result = d_neighbors(pattern, d)
for neighbor in result:
    print(neighbor)
