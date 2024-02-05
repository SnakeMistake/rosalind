f = open('rosalind_ba1h.txt',mode='r')
data = f.read().split()
# print(data)
pattern = data[0]
k = len(pattern)
genome = data[1]
d = int(data[2])


# pattern = "ATTCTGGA"
# genome = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC"
# k = len(pattern)
# d = 3


starting_positions = []

for i in range(len(genome)-k+1):
	counter = 0
	for x in range(len(genome[i:i+k])):
		if genome[i:i+k][x] != pattern[x]:
			counter+=1
	if counter <=d:
		starting_positions.append(str(i))

answer = " ".join(starting_positions)

print(answer)
		