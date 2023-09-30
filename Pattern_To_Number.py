def pattern_to_number(pattern):
    values = {'A': 0, "C": 1, "G": 2, "T": 3}
    number = 0
    for char in pattern:
        if char in values:
            number *= 4
            number += values[char]
        else: pass

    return number


with open('DNA_data.txt', 'r') as f1:
    lines = f1.read()

print(pattern_to_number(lines))