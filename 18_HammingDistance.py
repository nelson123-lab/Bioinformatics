def HammingDistance(string1, string2):
    count = 0
    for char1, char2 in zip(string1, string2):
        if char1 != char2:
            count += 1
        else: pass
    return count

string1 = "TCTCAATCGGACGAACATGATGAAGGACCGTCGTACAGCTGCTTAAGACTCAACGTGTCCACGGAAGGTAGTCTTTATGGACAATTGAGCTAGACGAAACTTATCTCCCTAATTTAGACGCTTTGCCCCGGTCGCTTTTATAAATGACATTAGGAGCAGCCAAACCGCGTAACCGAGTACGCCACGTTGTAGGCCTTGTGTCCCCCCTGTGGCTATCGCGAACCCTTAATCAGATCACATCAGCCGTTTTAGATAAGTATGATAACACTAATTATCCGAGACAGGGACCGAAACAGCGTGCTTGTGTTATAGCCGTTCCGCTTACCGAGCCTCTGGACGCAAAGTGTGGGACAGGTTAATTTAAAGATATTTCGGTGTCGTGACCACCATCGTGGTGGACATGGTGTACGACGTCGCCGGCAATTTCTGTTGTACCGGACACGGGTGCCGTAAAAGTCAGATTTACAGCTAGTGACCATGACTGAATCATTCACCCTGAAGTAATGCCCATTGGTTCAGCATAACTAGGCGCAGGTAACTACTCGGACATGTCGGAGTTTGACCAAACACGGTATCTAAGAAGAATACCAGATATGCGTCAACAGGCTCACTGTGGACGTAAAACTATCACGTTGTACCAAGGGCTTGTGGACGGTCTAAAAGTAATAGTAATATAAAATTTTGCGGATACGCCGAACCCCGTTAATCGTGTACGTAGCAGCCCGTCTAGACCCCAGAGATGTTTTGATACTCGCCATACAATCATAACGTGCTCCTGGCAACATGCTGCTTTTGTCTGACTAACAAGTCCGGAGCAGCGCGTGTTTTTATAGTATGTTGCCAGGTATAAAGATAAGAATAAGTGGTAGCGGTTGGTCTCATTCAATTGGCCGAGGTCGTACTTATGGCGCGCCCGGTTCACCAGTGATTTGGCCTTCGAACAGAAGCCTCGGAGTCCTCAGGAAGTGTCGACTCGACTTATTCTTGCTCATTTTGTTGTTCGAAGTCATTCCTATGCAACCCCTAATTGGCTTGAAGGTACATTACGTGGTCGTAAGGCTCCTTCGGCCACTTTCAAGTTCACCCCCTATAACGCCGCTCTTGCTTCTTTGT"
string2 = "TTGGGTCTGTGATCTCACTTATGAATAGACGGGTATCGTCTTAATATAGGACATCCCTGATCGCAGCTTAGATCCGTTTACGGGGGGACTACATACACTCATGTACCGGAACGACTTAAGATACCGACGAGACTGCACGTCGGTGTAGATGAACTCTCGGCCGGTGGAATGAAATGTGGCGTTTGGTTCAGACGAACGGCCCCGACAACTACGCGCTGTAGAGGCTGTGGGGAATAACGCGTCTTTTAATTATGGGTATAGATCCGAGCCCTGTCCCAAAAAGGCCCGTGAACGGGACTGACCTCTGCTTTGTCCGACCTGTCAATACTGACAGTACACCCCGGAGGAGGAGAGGCACACTCCCGATCATTTCGTGGGAATGGTCCGGATTTGGGACCAAGCTATAACGCAGAAATACACCAGTTTATATAAGCAGACTATCATTTCATACCAGGGGTGGGCGTTCAGTGATTCAACAATCTCTTGTGGCTTAAATGGCCCTCAGGTACCTTTTTGGTAGAGAGATAATAAGCGCCGGGAGACTCACCCAGGTACTCTGGTGATAGCGAGCCGATATGTGCAATGCAGTAGTGGGTTACCCCGAGTGTCGGCGAGAGACCTCGGTGGTAATAATTAGTGCATGGTGCAAAGAGAAGGCGAGTTCGAGCCTTGCACATGGTTAAGACCAGGGTGTACTGGGGCGCTTGTGGTGATTCAACTGCCGTGTCAGCTCACTGTGCGCAGATACGATACAACGCCATGCTTGGGTCAACGAGCCAACTTAGAGGAGCTTTTTAGTTATCATTGATCGATTATTAGGACGACCCTCGTCTTGCTCCCGAACAATCATGCCTTTGTTAGATTCTCGCCTTGCTGCACTACCAAGTAAATCCCTTGTGCCGGCTTTGTCATTAAGTCGGCCCGTCGCACTGATAACTTCTTAGATAGGCGTCAGTGCTTGGGTGTCCCTGGACTTGCGCTCGTCACCGCCTCGGCTGGTTACACGTTGGTGCAACGTATCTCTAATGCATCATTGTTACGTGCTACTGCTGGAACATGTCCCCTAATTAATACAACGGGTTGACAGTTGTTTGCGATTATCGGGCACAACCG"
print(HammingDistance(string1, string2))