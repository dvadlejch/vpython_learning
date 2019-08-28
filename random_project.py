from math import sqrt, exp, factorial
from random import random
import matplotlib.pyplot as plt

n = 10
x = []
for i in range(200):
    x.append( int(n*random()) )

plt.hist(x)
plt.show()
