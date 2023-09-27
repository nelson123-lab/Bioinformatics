def GC_content(string):
    count = 0
    if len(string) == 0:
        return 0
    else:
        length = len(string)
    for chr in string:
        if chr == "G" or chr == "C":
            count += 1
    return (count/length)*100

with open('DNA_data.txt', 'r') as f1:
    DNA_name = ""
    max_GC_content = 0
    DNA_string = ""
    lines = f1.read().split('\n')
    for line in lines:
        if line.startswith('>'):
            if DNA_name:
                GC = GC_content(DNA_string)
                if  GC > max_GC_content:
                    max_GC_content = GC
                    max_GC_DNA = DNA_name
            DNA_name = line[1:]
            DNA_string = ""
        else:
            DNA_string += line
    if DNA_name:
        GC = GC_content(DNA_string)
    if  GC > max_GC_content:
        max_GC_content = GC
        max_GC_DNA = DNA_name
    else: pass
    print(max_GC_DNA, max_GC_content, sep = "\n")