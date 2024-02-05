f = open('..\\data\\rosalind_ba1l.txt',mode="r")
data=f.read().split()
genome = data[0]
sample_genome = "AGT"

def pattern_to_number(dna):
	dnavalues = {"A":0,"C":1,"G":2,"T":3}
	value = 0
	for i in range(len(dna)):
		value+= dnavalues[dna[-1-i]]*4**i
	return value

print(pattern_to_number(genome))

