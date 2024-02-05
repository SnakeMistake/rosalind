from itertools import product

f = open("..\\data\\rosalind_ba1k.txt",mode="r")
data = f.read().split()
genome = data[0]
k = int(data[1])

sample_genome = "ACGCGGCTCTGAAA"
sample_k =2

def generate_possible_kmers(k):
	possible_kmers = []
	for item in product("ACGT",repeat=k):
		possible_kmers.append("".join(item))
	return possible_kmers

possible_kmers = generate_possible_kmers(k)
sample_possible_kmers = generate_possible_kmers(sample_k)


def generate_frequency_array(genome,k,possible_kmers):
	frequency_array = ""
	frequency_dict = {}
	for item in possible_kmers:
		frequency_dict[item] = 0
	for i in range(len(genome)-k+1):
		frequency_dict[genome[i:i+k]] = frequency_dict[genome[i:i+k]] + 1
	for item in frequency_dict.values():
		frequency_array += str(item)
		frequency_array += " "
	return frequency_array

# print(generate_frequency_array(sample_genome,sample_k,sample_possible_kmers))
print(generate_frequency_array(genome,k,possible_kmers))

