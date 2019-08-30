from random import random
import numpy as np
import matplotlib.pyplot as plt

#N = 1000 # number of steps

last_x = np.zeros(20)
dist_rms = np.zeros(8)
#t = np.arange(0, N)
k = 0
for N in [10, 50, 100, 200, 500, 1000, 1200, 1500]:
    for j in range(20):
        x = 0
        x_list = np.zeros(N)
        # random walk
        for i in range(N):
            ran_gen = random()
            if ran_gen > 0.5:
                x += 1
            else:
                x -= 1

            x_list[i] = x

        #--- plotting
        #plt.plot(t, x_list)

    # calculating of rms of the travelled distance
        last_x[j] = x_list[N-1]

    dist_rms[k] = np.sqrt( (last_x**2).mean() )
    print(dist_rms)
    k += 1
plt.plot([10, 50, 100, 200, 500, 1000, 1200, 1500], dist_rms)
plt.show()