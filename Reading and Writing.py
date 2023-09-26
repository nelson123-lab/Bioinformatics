with open('Sample_dataset.txt', 'r') as f_in:
    lines = f_in.readlines()
    even_lines = [lines for idx, lines in enumerate(lines, start = 1) if idx % 2 == 0]

with open('Output_dataset.txt', 'w') as f_out:
    f_out.writelines(even_lines)
