#This code should take a number of rabbit pairs (second number, k) and a number of generations (first number, n)
n,k = 30, 5
k_grow = [1]
k_grow.append(1+k)
k_grow.append(1+2*k)
for i in range(n-4):
 k_grow.append(k_grow[-1]+k_grow[-2]*k)
print(f"After {n} generations, starting with 1 rabbit, with {k} new rabbits born in each litter, there would be {k_grow[-1]} rabbits currently living")