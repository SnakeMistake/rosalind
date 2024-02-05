#This code should calculate the GC content of some DNA strings (the percent of the string that is composed of G and C) and should return the string with the HIGHEST GC value, along with its percentage of GC.  Note that this code works by accessing a .txt file titled "strands" with as many as 10 strands of many characters.  Part of the challenge here was figuring out how to access that file and slice the strands into useful pieces for performing the calculation.

with open('strands.txt') as strands:
 FASTA_strands = strands.read()
pairs_and_strands = []
percents = []

print(FASTA_strands)
def find_strings(strands, list):
 for i in range(strands.count(">")):
  list.append(strands[strands.find(">"):strands.find(">")+14])
  strands = strands[14:]
  if strands.find(">") > -1:
    list.append(strands[:strands.find(">")])
    strands = strands[strands.find(">"):]
  else:
     list.append(strands)
  
def calc_percent(list,percents):
 for i in range (len(list)):
   if i%2 == 1:
      percents.append(((list[i].count("G")+list[i].count("C"))/((list[i].count("G")+list[i].count("C")+list[i].count("A")+list[i].count("T")))))
      

find_strings(FASTA_strands, pairs_and_strands)
calc_percent(pairs_and_strands, percents)
print(f"The greatest GC content occurs in strand: {pairs_and_strands[percents.index(max(percents))*2]}")
print(f"The greatest percent for GC content is: {100*max(percents)}")