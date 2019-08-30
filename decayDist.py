from random import random
import numpy as np
import matplotlib.pyplot as plt
from math import factorial

# --- parameters
n = 10000
N = 5000
decay_prob = 0.001
n_prev = n
decay_number = np.zeros(N)
for j in range(N):
    n = n_prev
    for i in range(n):

        if random()<decay_prob:
            n -= 1

    decay_number[j] = n_prev - n

# --- plotting
def poisson(lam, k):
    p = np.zeros(len(k))
    for i in range(len(k)):
        fact = 1/factorial(k[i])
        p[i] = fact * lam**k[i] * np.exp(-lam)
    return p

k_range = np.arange(0, 40)
lam = 10
poiss = poisson(lam, k_range)

plt.hist(decay_number, bins=50, density=True)
plt.plot(k_range, poiss)
plt.show()