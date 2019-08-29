from random import random
import matplotlib.pyplot as plt
import numpy as np
from math import factorial

# ---- parameters
n = 120 # total number of molecules
t_max = 100000 # total number of simulated changes
n_left_list = []
t_list = np.arange(0, t_max)
n_left_arange = np.arange(0, n+1, 1)
#print(n_left_arange)
#--- one box full of molecules is connected to the other empty box
# left-hand is full whilst right-hand is empty at the beginning

n_left = n
t = 0
while t < t_max:
    molecule_number = int( (n+1)*random() ) # random choice whether the molecule is going from the left to the right or oposite
#    print(molecule_number)
#    print(n_left)

    if molecule_number > n_left:
        n_left += 1
    else:
        n_left -= 1

    n_left_list.append(n_left)
    t += 1

#---- plot
#plt.plot(t_list, n_left_list)
#plt.show()
bin_dist = []
factor1 = 1/2**n
factor2 = factorial(n)
for i in range(len(n_left_arange)):
    bin_dist.append( factor1*factor2/(factorial(n_left_arange[i])*factorial(n - n_left_arange[i])) )

plt.hist(n_left_list, density=True, bins=50)
plt.plot(n_left_arange, bin_dist)
plt.show()