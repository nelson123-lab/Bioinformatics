"""Function to process blast files"""
def process_blast_file(file_path):
    blast_results = {}
    with open(file_path, 'r') as blast_file:
        for line in blast_file:
            if line.strip():
                # Splitting the line into two parts at the first whitespace
                query_sequence, hit_sequence = line.split(maxsplit = 1)
                blast_results[query_sequence] = hit_sequence
    return blast_results

"""Function to find the reciprocal best blast hits"""
def find_reciprocal_bb_hits(blast_results_1, blast_results_2):
    # Initializing a dictionary to store the reciprocal best hits.
    reciprocal_hits = {}
    for query_sequence, hit_sequence in blast_results_1.items():
        if blast_results_2.get(hit_sequence) == query_sequence:
            reciprocal_hits[query_sequence] = hit_sequence
    return reciprocal_hits

"""Function to write the reciprocal best hits into txt files"""
def write_reciprocal_bbh(reciprocal_hits, output_file_path):
    with open(output_file_path, 'w') as f:
        for query_sequence, hit_sequence in reciprocal_hits.items():
            f.write(f"{query_sequence}\t{hit_sequence}\n")

output_file_path = 'outputF\Ldec_Tcas.txt'
blasthits_1 = process_blast_file('2_wayfiles\Agla_query_v_Ldec_subject.txt')
blasthist_2 = process_blast_file('2_wayfiles\Agla_query_v_Tcas_subject.txt')
rbbh = find_reciprocal_bb_hits(blasthits_1, blasthist_2)
write_reciprocal_bbh(rbbh, output_file_path)
print(f"Output files are present in {output_file_path}")
