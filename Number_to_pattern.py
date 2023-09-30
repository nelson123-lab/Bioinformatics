def number_to_pattern(index, k):
    values = {0: "A", 1: "C", 2: "G", 3: "T"}
    DNA_string = ""
    curr_state = 0
    for i in range(k):
            curr_state = index % 4
            DNA_string += values[curr_state]
            index //= 4

    return DNA_string[::-1]


with open('DNA_data.txt', 'r') as f1:
    lines = f1.read().split('\n')

index, k = map(int, lines)
print(number_to_pattern(index, k))