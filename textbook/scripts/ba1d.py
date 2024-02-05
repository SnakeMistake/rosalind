# by default, re searches for non-overlapping instances of a certain string/pattern.  I had to import regex as re to get an additional positional argument -- overlapped so that I could find overlapping instances.
import regex as re

# sample data to test
bases = "ATAT"
dna = "GATATATGCATATACTT"

# importing the files from rosalind and splitting into pattern and dna
f = open('rosalind_ba1d.txt',mode='r')
data =f.read().split()
# print(data)
target_dna = data[1]
base_sequence = data[0]


# output = re.finditer(bases, dna,overlapped=True)
# for item in output:
# 	print(item)
# 	print(item.span()[0])


# This returns an iterator with all of the match objects saved in it.  if you then iterate through that list, you can access the span of each object.  the first item in each span is the starting index, hence the [0]
output = re.finditer(base_sequence,target_dna, overlapped=True)
answer = ""
for item in output:
	answer+= str(item.span()[0])
	answer+= " "

print(answer)