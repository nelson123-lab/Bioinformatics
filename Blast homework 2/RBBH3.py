def read_blast_results(blast_file):
    with open(blast_file, 'r') as data:
        return {entry.split()[0]: entry.split()[1] for entry in data if entry.strip()}

def identify_3way_rbbh(species1_species2, species2_species3, species3_species1):
    reciprocal_hits = []
    for protein1, protein2 in species1_species2.items():
        protein3 = species2_species3.get(protein2)
        if protein3 and species3_species1.get(protein3) == protein1:
            reciprocal_hits.append((protein1, protein2, protein3))
    return reciprocal_hits

agla_tcas_file_path = 'Agla_query_v_Tdas_subject.txt'
tcas_ldec_file_path = 'Tdas_query_v_Ldec_subject.txt'
ldec_agla_file_path = 'Ldec_query_v_Agla_subject.txt'

agla_tcas_dict = read_blast_results(agla_tcas_file_path)
tcas_ldec_dict = read_blast_results(tcas_ldec_file_path)
ldec_agla_dict = read_blast_results(ldec_agla_file_path)

three_way_rbbh_results = identify_3way_rbbh(agla_tcas_dict, tcas_ldec_dict, ldec_agla_dict)

output_path = '3rbbh_results.txt'
with open(output_path, 'w') as f:
    for rbbh in three_way_rbbh_results:
        f.write('\t'.join(rbbh) + '\n')

print(f"3-way RBBH results written to {output_path}")