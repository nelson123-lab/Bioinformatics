with open('DNA_data.txt', 'r') as f1:
    lines = f1.readlines()
    string, pattern = lines[0], lines[1]

def count_occurrences(pattern, string):
    pattern_len = len(pattern)
    string_len = len(string)
    count = 0

    for i in range(string_len - pattern_len + 1):
        if string[i:i+pattern_len] == pattern:
            count += 1
    return count

occurrence_count = count_occurrences(pattern, string)
print(occurrence_count)