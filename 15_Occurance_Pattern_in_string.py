def Occurance_pattern(s, pattern):
    k = len(pattern)
    index = []
    for i in range(len(s)-k +1):
        if pattern == s[i:i+k]:
            index.append(i)
    return index

with open('DNA_data.txt', 'r') as f1:
    lines = f1.read().split('\n')
pattern, string  = lines[0], lines[1]
for i in Occurance_pattern(string, pattern):
    print(i, end = " ")