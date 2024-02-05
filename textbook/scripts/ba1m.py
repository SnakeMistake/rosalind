f = open('..\\data\\rosalind_ba1m.txt',mode='r')
data = f.read().split()
number_code = (int(data[0]), int(data[1]))
sample_num_code = (45,4) 

def number_to_pattern(tuple):
	pattern = ""
	value = tuple[0]
	k = tuple[1]
	dna_values = {"A":0,"C":1,"G":2,"T":3}
	for i in range(k):
		for base in "TGCA":
			if value >= dna_values[base]*(4**(k-1-i)):
				pattern += base
				value -= dna_values[base]*(4**(k-1-i))
				print(value)
				break
	return(pattern)

# print(number_to_pattern(sample_num_code))
print(number_to_pattern(number_code))

