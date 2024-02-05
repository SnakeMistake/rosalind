#This stores the raw data (strand, etc)
strand = "TTCAATGAAATTCAATGGGTTTCAATGCCTAATTTCAATGTTCAATGTACCTTCAATGAGTTCAATGCTTCAATGTTCAATGTTCAATGTTCAATGGTTCAATGTTCAATGAATTCAATGTAACTTCAATGTGGTCACGTTCAATGCTTCAATGCTTCAATGAGCTTTCAATGCAGTTTCATGTTCAATGTTCAATGCATTTCAATGTTTCAATGATTCAATGTTCAATGCTTAAATTTCAATGTGCAGGTTCAATGCATTCAATGCGGCCGACGGATGTTCAATGTTCAATGGTTCAATGGAATTCAATGCGCTTCAATGATGAAATATTCAATGATTCAATGCTTCAATGGGAATTCAATGTTCAATGTTCAATGTTTCAATGACTGGGCTATCGGCCCTGTTTCAATGAGCTTTCAATGTTTTCAATGGTTCAATGGGATTCAATGAACGACTTCAATGTTCAATGGCTTCAATGCCGTTTCAATGTTCAATGTTCAATGAGTTTCAATGTTCAATGGTTCAATGATTCAATGTTCAATGCCATTCAATGTAATTTTCAATGTCGATTACTTCAATGGGCTTCAATGCCTTCAATGGATCTTCAATGCTTCAATGTGGTTCAATGATTCAATGTTCAATGGGAAGAAGGAAACTACTTCAATGTTTCAATGTTCAATGTTTCAATGATGTTCAATGAGTTCAATGTGATTCAATGTTTTCAATGTTCAATGTGTTCAATGAGTTCAATGCGGTTATTCAATGGTGCTTCAATGGACTTTCAATGACGCGTCTTTCAATG"

#This code should look for a particular substring of DNA and will output all of the locations of that substring within a longer strand of DNA.abs

substrand = "TTCAATGTT"
strand_loc = []

for i in range(len(strand)):
  if strand[i:(i+len(substrand))] == substrand:
    strand_loc.append(i+1)
print(strand_loc)
