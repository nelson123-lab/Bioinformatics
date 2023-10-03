def most_freq_k_mers(DNA_string, k):
    
    kmersFreq = {}
    for i in range(len(DNA_string)-k +1):
        window = DNA_string[i:k+i]
        kmersFreq[window] = kmersFreq.setdefault(window, 1) + 1
    kmersFreq = dict(sorted(kmersFreq.items(), key = lambda x : (-x[1], x[0])))

    max_value = max(kmersFreq.values())
    most_freq = [key for key, values in kmersFreq.items() if values == max_value]
    return most_freq

with open('DNA_data.txt', 'r') as f1:
    lines = f1.read().split('\n')
DNA_string, k  = lines[0], int(lines[1])
for i in most_freq_k_mers(DNA_string, k):
    print(i, end = " ")