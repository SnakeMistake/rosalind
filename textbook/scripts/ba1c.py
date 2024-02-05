# Find the reverse complement of a dna strand

with open('rosalind_ba1c.txt') as f:
	contents = f.read()

print(contents)
dna = contents

practice_dna = "AAAACCCGGT"

def reverse_complement(dna):
	reverse_dna = dna[::-1]
	complement = ""
	for base in reverse_dna:
		if base == "A":
			complement += "T"
		elif base == "T":
			complement += "A"
		elif base == "G":
			complement += "C"
		elif base == "C":
			complement += "G"
	return complement

# print(reverse_complement(practice_dna))
print(reverse_complement(dna))