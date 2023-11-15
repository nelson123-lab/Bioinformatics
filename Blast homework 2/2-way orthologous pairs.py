import re

def read_blast_results(file_path):
    """
    Read BLAST results from a file and return a dictionary with query IDs as keys
    and lists of subject IDs as values.
    """
    blast_results = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue 
            fields = line.strip().split('\t')
            query_id, subject_id = fields[:2]
            if query_id not in blast_results:
                blast_results[query_id] = set()
            blast_results[query_id].add(subject_id)
    return blast_results

def find_rbbh(file1_results, file2_results):
    """
    Find Reciprocal Best BLAST Hits (RBBH) between two sets of BLAST results.
    """
    rbbh_pairs = []
    for query1, subjects1 in file1_results.items():
        for subject1 in subjects1:
            if subject1 in file2_results and query1 in file2_results[subject1]:
                rbbh_pairs.append((query1, subject1))
    return rbbh_pairs

def write_rbbh_to_file(rbbh_pairs, output_file):
    """
    Write RBBH pairs to an output file.
    """
    with open(output_file, 'w') as outfl:
        for pair in rbbh_pairs:
            outfl.write(f"{pair[0]}\t{pair[1]}\n")

def main():
    file1_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Module 5\Tcas_query_v_Ldec_subject.txt'
    file2_path = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Module 5\Ldec_query_v_Tcas_subject.txt'
    output_file = r'D:\Personal\Academics\UTA\3rd semester\Bioinformatics\Module 5\RBH-list-outfile_Tcas_Ldec.txt'

    file1_results = read_blast_results(file1_path)
    file2_results = read_blast_results(file2_path)
    rbbh_pairs = find_rbbh(file1_results, file2_results)
    write_rbbh_to_file(rbbh_pairs, output_file)
    print(f"Done. RBBH from {file1_path} and {file2_path} are in {output_file}")

if __name__ == "__main__":
    main()
