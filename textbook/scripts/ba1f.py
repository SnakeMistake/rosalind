# sample_genome = "CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"

f = open("rosalind_ba1f.txt",mode="r")
genome = f.read()
print(genome)

def skew_calc(genome):
	skew_list = []
	counter = 0
	for base in genome:
		if base == "G":
			counter+=1
		if base == "C":
			counter-=1
		skew_list.append(counter)
	return skew_list

skew_list = skew_calc(genome)
# print(skew_list)
minimum = min(skew_list)
# print(minimum)

minimum_list = []
for i in range(len(skew_list)):
	if skew_list[i] == minimum:
		minimum_list.append(i+1)

print(minimum_list)