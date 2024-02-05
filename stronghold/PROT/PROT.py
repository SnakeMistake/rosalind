mrna_strand = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
print(mrna_strand)
proteins = ""

while len(mrna_strand)>=3:
  if mrna_strand[:3] == "UUU":
    proteins += "F"
  if mrna_strand[:3] == "UUC":
    proteins += "F"
  if mrna_strand[:3] == "UUG":
    proteins += "L"
  if mrna_strand[:3] == "UUA":
    proteins += "L"
  if mrna_strand[:3] == "CUU":
    proteins += "L"
  if mrna_strand[:3] == "CUC":
    proteins += "L"
  if mrna_strand[:3] == "CUA":
    proteins += "L"
  if mrna_strand[:3] == "CUG":
    proteins += "L"
  if mrna_strand[:3] == "AUU":
    proteins += "I"
  if mrna_strand[:3] == "AUC":
    proteins += "I"
  if mrna_strand[:3] == "AUA":
    proteins += "I"
  if mrna_strand[:3] == "AUG":
    proteins += "M"
  if mrna_strand[:3] == "GUU":
    proteins += "V"
  if mrna_strand[:3] == "GUC":
    proteins += "V"
  if mrna_strand[:3] == "GUA":
    proteins += "V"
  if mrna_strand[:3] == "GUG":
    proteins += "V"
  if mrna_strand[:3] == "UCU":
    proteins += "S"
  if mrna_strand[:3] == "UCC":
    proteins += "S"
  if mrna_strand[:3] == "UCA":
    proteins += "S"
  if mrna_strand[:3] == "UCG":
    proteins += "S"
  if mrna_strand[:3] == "CCU":
    proteins += "P"
  if mrna_strand[:3] == "CCC":
    proteins += "P"
  if mrna_strand[:3] == "CCA":
    proteins += "P"
  if mrna_strand[:3] == "CCG":
    proteins += "P"
  if mrna_strand[:3] == "ACU":
    proteins += "T"
  if mrna_strand[:3] == "ACC":
    proteins += "T"
  if mrna_strand[:3] == "ACA":
    proteins += "T"
  if mrna_strand[:3] == "ACG":
    proteins += "T"
  if mrna_strand[:3] == "GCU":
    proteins += "A"
  if mrna_strand[:3] == "GCC":
    proteins += "A"
  if mrna_strand[:3] == "GCA":
    proteins += "A"
  if mrna_strand[:3] == "GCG":
    proteins += "A"
  if mrna_strand[:3] == "UAU":
    proteins += "Y"
  if mrna_strand[:3] == "UAC":
    proteins += "Y"
  if mrna_strand[:3] == "UAA":
    proteins += " Stop "
  if mrna_strand[:3] == "UAG":
    proteins += " Stop "
  if mrna_strand[:3] == "CAU":
    proteins += "H"
  if mrna_strand[:3] == "CAC":
    proteins += "H"
  if mrna_strand[:3] == "CAA":
    proteins += "Q"
  if mrna_strand[:3] == "CAG":
    proteins += "Q"
  if mrna_strand[:3] == "AAU":
    proteins += "N"
  if mrna_strand[:3] == "AAC":
    proteins += "N"
  if mrna_strand[:3] == "AAA":
    proteins += "K"
  if mrna_strand[:3] == "AAG":
    proteins += "K"
  if mrna_strand[:3] == "GAU":
    proteins += "D"
  if mrna_strand[:3] == "GAC":
    proteins += "D"
  if mrna_strand[:3] == "GAA":
    proteins += "E"
  if mrna_strand[:3] == "GAG":
    proteins += "E"
  if mrna_strand[:3] == "UGU":
    proteins += "C"
  if mrna_strand[:3] == "UGC":
    proteins += "C"
  if mrna_strand[:3] == "UGA":
    proteins += " Stop "
  if mrna_strand[:3] == "UGG":
    proteins += "W"
  if mrna_strand[:3] == "CGU":
    proteins += "R"
  if mrna_strand[:3] == "CGC":
    proteins += "R"
  if mrna_strand[:3] == "CGA":
    proteins += "R"
  if mrna_strand[:3] == "CGG":
    proteins += "R"
  if mrna_strand[:3] == "AGU":
    proteins += "S"
  if mrna_strand[:3] == "AGC":
    proteins += "S"
  if mrna_strand[:3] == "AGA":
    proteins += "R"
  if mrna_strand[:3] == "AGG":
    proteins += "R"
  if mrna_strand[:3] == "GGU":
    proteins += "G"
  if mrna_strand[:3] == "GGC":
    proteins += "G"
  if mrna_strand[:3] == "GGA":
    proteins += "G"
  if mrna_strand[:3] == "GGG":
    proteins += "G"
  mrna_strand = mrna_strand[3:]
print(proteins)