sample_k=3
sample_t= 5

sample_Dna = [
"GGCGTTCAGGCA",
"AAGAATCAGTCA",
"CAAGGAGTTCGC",
"CACGTCAATCAC",
"CAATAATATTCG"
]


def greedymotifsearch(dna,k,t):
	best_motifs = [strand[:k] for strand in dna]
	print(best_motifs)
	for i in range(len(dna[0])-k+1):
		motif = dna[0][i:i+k]
		print(motif)
		profile = gen_profile(best_motifs[0],dna)



def calc_hamming(motif,kmer):
	dist = 0
	for i in range(len(motif)):
		if motif[i] != kmer[i]:
			dist+=1
	return dist


print(calc_hamming("cda","cda"))

def gen_profile(motif,dna):
	profile = [[0 for i in range(len(motif))]]*4
	print(profile)
	for strand in dna:
		for i in range(len(strand)-len(motif)+1):
			kmer = strand[i:i+len(motif)]
			for i,base in enumerate(kmer):
				pass



greedymotifsearch(sample_Dna,sample_k,sample_t)