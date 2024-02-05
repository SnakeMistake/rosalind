### Importing the rosalind file:
f = open('rosalind_ba1e.txt', mode='r')
contents = f.read()
variables = contents.split()
# print(variables)
genome = variables[0]
k = int(variables[1])
L = int(variables[2])
t = int(variables[3])

# Variables for testing:
sample_genome= "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"
sample_k = 5
sample_L = 75
sample_t = 4

# list for tracking the pattern matches:
clump_patterns = []

def check_window_L(k,L,t, genome,clump_patterns):
	patterns = []
	for i in range(len(genome)-k):
		patterns.append(genome[i:i+k])
		# print(patterns)
		if i > L-k:
			patterns.pop(0)
			# lost_pattern = patterns.pop(0)
			# print(lost_pattern)
			if patterns.count(genome[i:i+k]) >= t and genome[i:i+k] not in clump_patterns:
				clump_patterns.append(genome[i:i+k])

# check_window_L(sample_k,sample_L,sample_t,sample_genome,clump_patterns)
check_window_L(k,L,t,genome,clump_patterns)

answer = ""
for pattern in clump_patterns:
	answer += pattern
	answer += " "

print(answer)
		
			