def find_occurrences(Pattern, Genome):
    occurrences = []  # Step 1
    
    for i in range(len(Genome) - len(Pattern) + 1):  # Step 2
        if Genome[i:i+len(Pattern)] == Pattern:  # Step 3
            occurrences.append(i)
    
    return occurrences  # Step 4

# Example usage
Pattern = "ATAT"
Genome = "GATATATGCATATACTT"
result = find_occurrences(Pattern, Genome)
print(result)
