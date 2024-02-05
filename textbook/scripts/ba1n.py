from itertools import combinations, product

data = open('..\\data\\rosalind_ba1n.txt',mode="r").read().split()
pattern=data[0]
d = int(data[1])

test_pattern = "ACG"
test_d = 1

def generate_indices(pattern,d):
	length = len(pattern)
	indices = []
	for i in range(d+1):
		for item in combinations(range(length),i):
			indices.append(item)
	return indices 

indices = generate_indices(pattern,d)
indices.pop(0)

def generate_d_neighborhood(pattern,indices):
	d_neighborhood = []
	pattern_list = list(pattern)
	d_neighborhood.append(pattern)
	for index_list in indices:
		r = len(index_list)
		base_combos = []
		for item in product("ACGT",repeat=r):
			base_combos.append(item)
		for combo in base_combos:
			for i in range(len(combo)):
				pattern_list[index_list[i]] = combo[i]
			new_pattern = "".join(pattern_list)
			if new_pattern not in d_neighborhood:
				d_neighborhood.append("".join(pattern_list))
			pattern_list = list(pattern)
	return d_neighborhood 


# d_neighborhood = generate_d_neighborhood(pattern,indices)
# print(len(d_neighborhood))

# answer = ""
# for pattern in d_neighborhood:
# 	answer += pattern
# 	answer += "\n"
# print(answer)


# NOTE - this rosalind problem ONLY accepted answers with each possibility printed on a new line, rather than answers printed with spaces inbetween
# as it has for other problems.  As a result... I wasted a bunch of time with the alternate code below.  I was avoiding doing this because it was less efficient.
# Turns out that was a good move - it takes too long to run and wouldn't generate any answers ---







# Alternate method -- generate all possible k-mers and then pull out the ones that have d+ differences....
# def generate_possible_kmers(k):
# 	possible_kmers = []
# 	for item in product("ACGT",repeat=k):
# 		possible_kmers.append("".join(item))
# 	return possible_kmers

# possible_kmers = generate_possible_kmers(len(pattern))
# print(len(possible_kmers))

# def weed_out_d_plus(pattern,possibilities,d):
# 	for possibility in possibilities:
# 		counter = 0
# 		for i in range(len(possibility)):
# 			if possibility[i] != pattern[i]:
# 				counter +=1
# 		if counter > d:
# 			possibilities.remove(possibility)
# 	return possibilities

# print(weed_out_d_plus(pattern,possible_kmers,test_d))

# Here's my attempt at the recursive solution from the book.  I'm basically taking their pseudocode and translating it line by line into python: 
def neighbors(pattern,d):
	# print("loop")
	# print(pattern)
	if d == 0:
		return pattern 
	if len(pattern) == 1:
		return ["A","C","G","T"]
	neighborhood = set()
	# print(neighborhood)
	suffix_neighbors = neighbors(pattern[1:],d)
	# print(suffix_neighbors)
	for suffix in suffix_neighbors:
		# print(suffix)
		# print(pattern[1:])
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

print(neighbors("ACGT",1))
# print(neighbors(pattern,d))
