data = open('..\\data\\rosalind_ba2a.txt').read().split()
k = int(data[0])
d = int(data[1])
strands = data[2:]
# print(strands)

sample_k=3
sample_d=1
sample_strands=["ATTTGGC",
"TGCCTTA",
"CGGTATC",
"GAAAATT"]


def neighbors(pattern,d):
	if d == 0:
		return pattern
	if len(pattern) ==1:
		return ["A","C","G","T"]
	neighborhood = set()
	suffix_neighbors = neighbors(pattern[1:],d)
	for suffix in suffix_neighbors:
		hamming_dist = 0
		for i in range(len(suffix)):
			if suffix[i] != pattern[1:][i]:
				hamming_dist += 1
		if hamming_dist < d:
			for base in "ACGT":
				neighborhood.add(base + suffix)
		else:
			neighborhood.add(pattern[0]+suffix)
	return neighborhood


def check_neighbors_against_strands(k,d,strands):
	motifs = set()
	for i in range(len(strands[0])-k+1):
		pattern = strands[0][i:i+k]
		candidates = neighbors(pattern,d)
		for candidate in candidates:
			count = 0
			for strand in strands:
				pool = set()
				for i in range(len(strand)-k+1):
					new_additions = neighbors(strand[i:i+k],d)
					for item in new_additions:
						pool.add(item)
				if candidate in pool:
					count += 1
			if count == len(strands):
				motifs.add(candidate)
	return motifs 


# print(check_neighbors_against_strands(sample_k,sample_d,sample_strands))
answers = check_neighbors_against_strands(k,d,strands)
output = ""
for answer in answers:
	output += answer
	output += " "
print(output)
print("done")


	
