#This code should take value for m (the number of months the rabbit pairs live) and a number of months that they reproduce (first number, n)

n,m = 94, 16
pop_tot = [1,1,2]
babies = [1,0,1]
death = [0,0,0]
for i in range(n-3):
  growth = (pop_tot[-1]-babies[-1])
  if len(pop_tot) >= m:
    dead = babies[-(m)]
    death.append(dead)
  else:
    death.append(0)
  babies.append(growth)
  pop_tot.append(growth - death[-1] + pop_tot[-1])
  

# print(pop_tot)
# print(babies)
# print(death)
print(f"After {n} months, starting with 1 rabbit, with rabbits dying after {16} months, there would be {pop_tot[-1]} rabbits currently living")