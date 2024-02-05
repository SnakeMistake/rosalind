with open('strands.txt') as strands:
 fs_strands = strands.read()
titles = []
dna_strands = []
g_count =[]
c_count = []
a_count = []
t_count = []

def split_source(source, titles, dna_strands):
  x = -1
  list = source.split()
  for i in range(source.count(">")):
    dna_strands.append("")
  for term in list:
    if term[0] == ">":
      x +=1
      titles.append(term[1:])
    else:
      dna_strands[x] += term
split_source(fs_strands, titles, dna_strands)
print(dna_strands)
print(titles)

for x in range(len(dna_strands[0])):
  g_count.append(0)
  c_count.append(0)
  a_count.append(0)
  t_count.append(0)


def count_bases(dna_strands, g_count, c_count, a_count, t_count):
  for i in range(len(dna_strands)):
    for index,base in enumerate(dna_strands[i]):
      if base == "G":
        g_count[index] += 1
      if base == "A":
        a_count[index] += 1
      if base == "C":
        c_count[index] += 1
      if base == "T":
        t_count[index] += 1
        
count_bases(dna_strands, g_count, c_count, a_count, t_count)
print(g_count)
def con_string(g_count, c_count, a_count, t_count):
  strand = ""
  for i in range(len(g_count)):
    if g_count[i] >= c_count[i] and g_count[i] >= a_count[i] and g_count[i] >= t_count[i]:
      strand += "G"
    elif c_count[i] >= a_count[i] and c_count[i] >= t_count[i]:
      strand += "C"
    elif a_count[i] >= t_count[i]:
      strand += "A"
    else:
      strand += "T"
  return strand

def cleanup(count_list):
  base_count = ""
  for i in range(len(count_list)):
    base_count += f"{count_list[i]} "
  return base_count
g_list = cleanup(g_count)
a_list = cleanup(a_count)
c_list = cleanup(c_count)
t_list = cleanup(t_count)
print(g_list)
consensus_string = con_string(g_count, c_count, a_count, t_count)
print(consensus_string)
print(f"A: {a_list}")
print(f"C: {c_list}")
print(f"G: {g_list}")
print(f"T: {t_list}")