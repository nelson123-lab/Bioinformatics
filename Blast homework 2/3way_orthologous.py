import pandas as pd

"""Function to preprocess the files and convert them into dictionaries"""
def pre_process(filename):
    data = pd.read_csv(filename, sep='\t')
    data = data.iloc[:, :2]
    keys = data.iloc[:, 0].tolist()
    values = data.iloc[:, 1].tolist()
    my_dict = dict(zip(keys, values))
    return my_dict

"""Function to flip the dictiionary"""
def flipped(dictionary): # key -> value, value -> key
    return {value: key for key, value in dictionary.items()}

"""Function to find the rbbh"""
def find_rbbh(file1_results, file2_results, file3_results):
    rbbh = []
    file2_results_F = flipped(file2_results) # T L 
    for file1_key, file1_value in file1_results.items(): # A T
        if file1_value in file2_results_F.keys(): # T L
            file2_value = file2_results_F[file1_value] # L
            if file2_value in file3_results: # L A
                file3_value = file3_results[file2_value] # A
                if file3_value in file1_results and file3_value == file1_key:
                    rbbh.append([file3_value, file1_value, file2_value])
    return rbbh

file1_results = pre_process('output1\RBH-list-outfile_Agla_Tcas.txt') # Agla_Tcas
file2_results = pre_process('output1\RBH-list-outfile_Ldec_Tcas.txt') # Ldec_Tcas
file3_results = pre_process('output1\RBH-list-outfile_Ldec_Agla.txt')

# A T 
# L T
# L A # A L
rbbh = find_rbbh(file1_results, file2_results, file3_results)
df = pd.DataFrame(rbbh, columns=['Agla', 'Tcas', 'Ldec'])
