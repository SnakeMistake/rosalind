f = open('rosalind_ba1g.txt',mode='r')
data = f.read().split()
genome1 = data[0]
genome2 = data[1]

counter = 0
for i in range(len(genome1)):
	if genome1[i] != genome2[i]:
		counter +=1
print(counter)