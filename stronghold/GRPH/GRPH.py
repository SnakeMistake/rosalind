target_dict= {}
adjac_list = {}
test_dict_one = {"Rosalind_0498" : "AAATAAA",
"Rosalind_2391" : "AAATTTT",
"Rosalind_2323" : "TTTTCCC",
"Rosalind_0442" : "AAATCCC",
"Rosalind_5013" : "GGGTGGG"}

test_dict_two = {"Rosalind_0498" : "AAATAAA",
"Rosalind_2456" : "ATATCCC",
"Rosalind_1234" : "TCGAAA",
"Rosalind_5520" : "AAACGGG",
"Rosalind_3219" : "CCCACAC"}

test_dict_three = {"Rosalind_3250" : "AGGGACC",
"Rosalind_3451":"ACGCGCGCT"}

test_dict_four = {"Rosalind_3219" : "GGGACACCCG"} 

test_dict_five = {"Rosalind_0498" : "AATTAAT",
"Rosalind_2456" : "ATATCCC",
"Rosalind_1234" : "TCGAAA",
"Rosalind_5520" : "AAACGGG",
"Rosalind_3219" : "GCGACAC",
"Rosalind_5812" : "CGCTACA"}

test_dict_six = {"Rosalind_1234" : "AAATAAA" 
, "Rosalind_1235" : "AAAGAAA"}

with open('rosalind_grph.txt') as strands:
 fs_strands = strands.read()

def split_source(source, target_dict):
  list = source.split()
  for i,term in enumerate(list):
    if term[0] == ">":
      target_dict[term[1:]] = "".join(list[i+1] + list[i+2])
    else:
      pass
split_source(fs_strands, target_dict)


def diff_check(strand_one, strand_two):
  if strand_one[-3:] == strand_two[:3]:
    print(f"Ending: {strand_one[-3:]} & Beginning: {strand_two[:3]} ")
    return True
  else:
    return False
    
def adj_check(dict):
  for strand in dict:
    for other_strand in dict:
      if strand != other_strand:
        if diff_check(dict[strand], dict[other_strand]) == True:
          if strand not in adjac_list:
            adjac_list[strand] = [other_strand]
          else: 
            adjac_list[strand].append(other_strand)
  for term in adjac_list:
    for strand in adjac_list[term]:
      print(f"{term} {strand}")

adj_check(target_dict)