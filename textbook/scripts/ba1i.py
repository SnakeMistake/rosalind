from itertools import product

f = open('..\\data\\rosalind_ba1i.txt',mode="r")
data = f.read().split()
genome = data[0]
k = int(data[1])
d = int(data[2])
# print(data)


sample_genome="ACGTTGCATGTCGCATGATGCATGAGAGCT"
sample_k =4
sample_d =1



def findkmers(genome,k):
	kmers=[]
	for i in range(len(genome)-k+1):
		kmers.append(genome[i:i+k])
	return kmers

# I missed this entire idea from the outset -- the most frequent 'match' in a genome might actually be a pattern that doesn't exist in that genome
# for that reason, I generated all theoretical patterns here (permutations of ATGC, length k) using itertools and then compared that
# against the kmers that actually existed in the real genome
def genpossiblekmers(k):
	possible_kmers =[]
	for item in product("ATGC",repeat=k):
		possible_kmers.append("".join(item))
	return possible_kmers

possiblekmers = genpossiblekmers(k)
kmers=findkmers(genome,k)

def findnearmatches(possiblekmers, kmers,d):
	max_matches = 0
	match_list = []
	for kmer in possiblekmers:
		matches = 0
		for otherkmer in kmers:
			diffs = 0
			for i in range(len(kmer)):
				if kmer[i] != otherkmer[i]:
					diffs+=1
			if diffs <=d:
				matches+=1
		if matches > max_matches:
			match_list = [kmer]
			max_matches = matches
		elif matches == max_matches:
			match_list.append(kmer)
	return " ".join(match_list)


match_list = (findnearmatches(possiblekmers, kmers,d))
print(match_list)
