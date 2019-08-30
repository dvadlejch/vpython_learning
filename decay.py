from random import random
import numpy as np
import matplotlib.pyplot as plt

# --- parameters
n = 10000
decay_prob = 0.001
tmax = 5000
t = np.arange(0, tmax)
n_list = np.zeros(len(t))

# --- time step
for j in t:

    for i in range(n):

        if random() < decay_prob:
            n -= 1


    n_list[j] = n

# -- plotting
plt.plot(t, n_list)
plt.show()
