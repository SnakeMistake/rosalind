#This code should simulate mendelian genetics by calculating probability of having a dominant allele.  k represents homozygous dominant.  m represents heterozygous.  n represents homozygous recessive
k, m, n = 17, 20, 27
total = k + m + n
kk = (k/total)*((k-1)/(total-1))
km = (k/total)*(m/(total-1))
kn= (k/total)*(n/(total-1))
mm= (m/total)*((m-1)/(total-1))
mn= (m/total)*((n)/(total-1))
mk= (m/total)*((k)/(total-1))
nn= (n/total)*((n-1)/(total-1))
nm = (n/total)*((m)/(total-1))
nk = (n/total)*((k)/(total-1))
wtdprob = (kk+km+kn+mk+nk)+(mm)*.75+(mn+nm)*.50
print(total)
print(f"The probability of getting a dominant allele with this population is {wtdprob}")
