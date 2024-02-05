f = open("..\\data\\rosalind_ba2c.txt",mode="r").read().split()

text = f[0]
k = int(f[1])
profile = f[2:]


sample_text ="ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
sample_k= 5
sample_profile_data ="0.2 0.2 0.3 0.2 0.3 0.4 0.3 0.1 0.5 0.1 0.3 0.3 0.5 0.2 0.4 0.1 0.2 0.1 0.1 0.2"
sample_profile = sample_profile_data.split()


def handle_profile(profile, k):
	profile_matrix = []
	counter = 0
	current_line = []
	for item in profile:
		current_line.append(float(item))
		counter += 1
		if counter % k == 0:
			profile_matrix.append(current_line)
			current_line = []
	return profile_matrix

# sample_profile_matrix =handle_profile(sample_profile,sample_k)
profile_matrix = handle_profile(profile,k)



def generate_k_mers(text,k):
	kmers = []
	for i in range(len(text)-k+1):
		kmer = text[i:i+k]
		kmers.append(kmer)
	return kmers 

k_mers = generate_k_mers(text,k)
# print(k_mers)

def calc_prob_kmer(k_mer,profile):
	probability = 1
	for i,letter in enumerate(k_mer):
		if letter == "A":
			probability *= profile[0][i]
		if letter == "C":
			probability *= profile[1][i]
		if letter == "G":
			probability *= profile[2][i]
		if letter == "T":
			probability *= profile[3][i]
	return probability

def find_most_probable(k_mers,profile):
	highest_prob = 0
	most_probable_kmer = ""
	for k_mer in k_mers:
		prob = calc_prob_kmer(k_mer,profile)
		if prob > highest_prob:
			highest_prob = prob 
			most_probable_kmer = k_mer
			print(k_mer)
			print(prob)
	return most_probable_kmer



print(find_most_probable(k_mers,profile_matrix))