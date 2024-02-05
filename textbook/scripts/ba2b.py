from itertools import product

data = open("..\\data\\rosalind_ba2b.txt",mode="r").read().split()
k = int(data[0])
dna = data[1:]

print(k)
print(dna)


sample_k = 3
sample_strands = [
"AAATTGACGCAT",
"GACGACCACGTT",
"CGTCAGCGCCTG",
"GCTGAGCACCGG",
"AGTACGGGACAG"]

def d(pattern,text):
	min_dist = 100
	k = len(pattern)
	for i in range(len(text)-k+1):
		dist = hamming_dist(pattern,text[i:i+k])
		if dist < min_dist:
			min_dist= dist 
	return min_dist


def hamming_dist(pattern,strand):
	count=0
	for i in range(len(pattern)):
		if pattern[i] != strand[i]:
			count+=1
	return count


def total_dist(pattern, dna):
	total_distance = 0
	for i in range(len(dna)):
		total_distance += d(pattern,dna[i])
	return total_distance

def find_median_string(k,dna):
	kmers = []
	min_d = 100
	median_string = ""
	for item in (product("ACGT",repeat=k)):
		kmers.append("".join(item))
	for kmer in kmers:
		total_distance = total_dist(kmer,dna)
		if total_distance < min_d:
			min_d = total_distance
			median_string=kmer
			print(min_d)
			print(median_string)
	return median_string



# print(hamming_dist("AGTCT", "AGTGA"))
# print(d("AAA",sample_strands[4]))
# print(total_dist("GAC",sample_strands))
# find_median_string(sample_k,sample_strands)

find_median_string(k,dna)
