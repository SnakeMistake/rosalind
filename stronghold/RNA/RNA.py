strand = "AAGCCGCGCCGCGGGTACTTTGATACCCATACCTACAACTGGCAAAACCGGGACTGTATCGATGTGACCTATATGGTCTGGGGTCTCATTCAATACATGGTGGACTGGGCTAGCGGAAGACGCCTCAGGTGCGCTATCCGTACGGTCCTTCCTGGAGGTCCCGGCGGAAGAGTGGGGTAAGTGCTGGGATGGTGCAACGCTAGTGCCTTTGTCGTTGGAGGTACTATCAGCCAAGAGGCATCGAAGCCAATGGATTCAGCGCCGCTACATTAACACACCCCGACGATTAACTCTGCGCCAAGCCGATTCCGCTGGGTTGGTGGACTTGGTATAGTGGGAAACTGAGCGTGTCGCTAAATGGGTGCGCATAGTTAGTCTGCTACTAACTTGCGAAGTGCTCGCACATAAACCTTGGGACGGAATGCTTCCCCAGGTCCTTGCACTCCTCACCGTAAGTTCTATCGTGGTTCAGTCGGTTTTCCTTGAGCCATTTCTTAGAGGTGTCACACTGAGTGCCGACATACCATTGTCAGAAGTAAGGAAAGCCGAATGCAGTCAATCAACACTTGGGCTTCATAATAGGCTACGTTAATGATACCCATACATCGTGATACGATTCATCGCAGGGTACGGATGCGAGTCAAGGTTAGTCTTTCTCCACATATGCCCGCGGGCCGATCTGTACACCGAACGCTAACAAGCCTCGCGTCAAGTGGGCAGTCCTGCAAACATCCGGTGGTTTCTAAGAGCACCGGTTAGTTGACCATTGGACGAGCCGTCCTCGGCGTATTCCAACAGCTTCCTCGAGAGAATACGTTGACTGAAAAAGACGTAAGTAAAGCGTGCGTTAATGCTATAATAAAGTGGCCGGG"

#This code should convert DNA into RNA by swapping T for U:
print('this creates RNA from DNA: ')
RNA = strand.replace("T","U")
print(RNA)
