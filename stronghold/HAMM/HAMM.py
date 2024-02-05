#This code should find something called the Hamming distance - which is basically just the number of bases different between two strings

string1 = "AGCGGAACG"
string2 = "AGGGTAAAT"
mut_count = 0
for index, base in enumerate(string1):
 if string1[index] != string2[index]:
   mut_count +=1
print(mut_count)
