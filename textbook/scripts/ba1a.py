# file cleanup -- opening a text file and splitting the two 'new line' segments into a dna strand and a target pattern
with open('rosalind_ba1a.txt') as dna:
	contents = dna.read()
data = contents.split()

dna = data[0]
pattern = data[1]


def count_patterns(text,pattern):
	count = 0
	for i in range(len(text)-len(pattern)+1):
		if text[i:i+len(pattern)] == pattern:
			count += 1
	return count


print(count_patterns(dna, pattern))
	