from itertools import product
f = open("..\\data\\rosalind_ba1j.txt",mode="r")
data = f.read().split()
genome = data[0]
k = int(data[1])
d = int(data[2])
# print(data)

sample_genome= "ACGTTGCATGTCGCATGATGCATGAGAGCT"
sample_k =4
sample_d = 1



def genpossiblekmers(k):
	possible_kmers=[]
	for item in product("ATGC",repeat=k):
		possible_kmers.append("".join(item))
	return possible_kmers
possiblekmers = genpossiblekmers(k)
sample_possible = genpossiblekmers(sample_k)
# print(sample_possible)

# def forwardandreversekmers(genome,k):
# 	kmers = []
# 	reverse_kmers = []
# 	reverse_complements = []
# 	patterns = []
# 	reverse_genome = genome[::-1]
# 	for i in range(len(genome)-k+1):
# 		kmers.append(genome[i:i+k])
# 		reverse_kmers.append(reverse_genome[i:i+k])
# 	for item in reverse_kmers:
# 		complement = item.replace("A","t").replace("G","c").replace("T","a").replace("C","g").upper()
# 		reverse_complements.append(complement)
# 	# print(kmers)
# 	# print(reverse_kmers)
# 	# print(reverse_complements)
# 	patterns.extend(kmers)
# 	patterns.extend(reverse_complements)
# 	# print(patterns)
# 	return patterns
# # kmers = forwardandreversekmers(genome,k)
# sample_kmers = forwardandreversekmers(sample_genome,sample_k)
# # print(sample_kmers)

def findkmers(genome,k):
	kmers=[]
	for i in range(len(genome)-k+1):
		kmers.append(genome[i:i+k])
	return kmers
kmers=findkmers(genome,k)
sample_kmers = findkmers(sample_genome,sample_k)


def checkmatches(possiblekmers,kmers,d):
	max_matches = 0
	match_list = []
	for kmer in possiblekmers:
		matches=0
		for otherkmer in kmers:
			diffs = 0
			reverse_kmer = kmer[::-1].replace("A","t").replace("G","c").replace("T","a").replace("C","g").upper()
			# print(kmer,reverse_kmer)
			for i in range(len(kmer)):
				if kmer[i] != otherkmer[i]:
					diffs+=1
			if diffs <= d:
				matches +=1
			diffs = 0
			for i in range(len(kmer)):
				if reverse_kmer[i] != otherkmer[i]:
					diffs +=1
			if diffs <= d:
				matches +=1
		if matches > max_matches:
			match_list = [kmer]
			max_matches = matches
		elif matches == max_matches and kmer not in match_list:
			match_list.append(kmer)
		else:
			pass
	return " ".join(match_list)

print(checkmatches(possiblekmers,kmers,d))
print(checkmatches(sample_possible,sample_kmers,sample_d))



		
