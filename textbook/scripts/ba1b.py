sample_dna = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
# opening the rosalind file and saving the two items as a dna string and an integer k (the length of the pattern)
with open('rosalind_ba1b.txt') as f:
	contents = f.read()
data = contents.split()
dna = data[0]
k = int(data[1])

# makes a dictionary for every string of length k (moving in a weindow through the text) -- if the string already exists, it adds a count of 1.  Otherwise it starts with a count of 1.
def find_k_mers(text,k):
	k_mers = {}
	for i in range(len(text)-k):
		if text[i:i+k] not in k_mers:
			k_mers[text[i:i+k]] = 1
		else:
			k_mers[text[i:i+k]] = k_mers[text[i:i+k]] +1
	return k_mers

print(find_k_mers(dna,k))
# print(find_k_mers(sample_dna,4))

# Sorts through the dictionary keys to find the largest associated value and  any string with that count.
def find_max(k_dict):
	max = 0
	max_list = []
	for key in k_dict:
		if k_dict[key] > max:
			max_list = [key]
			max = k_dict[key]
		elif k_dict[key] == max:
			max_list.append(key)
	return max_list

print(find_max(find_k_mers(dna,k)))
# print(find_max(find_k_mers(sample_dna,4)))
		