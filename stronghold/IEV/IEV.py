'''
This dictionary gives the odds of a dominant phenotype for each pair:
AA-AA - 100%
AA-Aa - 100%
AA-aa - 100%
Aa-Aa - 75%
Aa-aa - 50%
aa-aa - 0%
That corresponds to 2 offspring, 1.5 offspring, 1 offspring and 0 offspring
'''
pheno_probs ={
	"1":2,
	"2":2,
	"3":2,
	"4":1.5,
	"5":1,
	"6":0
}
#These first list is the sample problem.  The second list I copy/pasted from Rosalind.
test_list = [1, 0, 0, 1, 0, 1]
target_list = [19882, 19898, 19127, 17349, 19980, 18130]
#This function iterates through the list and multiplies each number of couples by its corresponding offspring output
def calc_offspring(list):
	sum = 0
	for i in range(6):
		sum += pheno_probs[str(i+1)]*list[i]
	return sum

print(calc_offspring(target_list))
	