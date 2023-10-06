# Finding all possible combinations of DNA base with length = k
def Generate_kmer(k):
    DNAbases = ['A', 'C', 'G', 'T']
    for _ in range(k - 1):
        DNAbases = [(i + j) for i in DNAbases for j in DNAbases]
    return DNAbases

# Finding the count of each kmer within the DNA_string
def PatternCount(DNA_string, Pattern):
    # Finding the count each time and returning it since it runs within a for loop.
    Count = sum(1 for i in range(len(DNA_string) - len(Pattern) + 1) if DNA_string[i:i+len(Pattern)] == Pattern)
    return Count

# Finding the frequencey array that holds the number of times that the i-th kmer appears in the string.
def Frequency_array(DNA_string, k):
    # Generating the frequency array
    Freq_array = [PatternCount(DNA_string, pattern) for pattern in Generate_kmer(k)]
    # Printing the output in the required format as strings.
    print(" ".join(map(str, Freq_array)))

if __name__ == "__main__":
    with open("DNA_data.txt", "r") as f1:
        DNA_string = f1.readline().strip()
        k = int(f1.readline().strip())
    Frequency_array(DNA_string, k)