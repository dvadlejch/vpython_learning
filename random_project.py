from math import sqrt, exp, factorial
from random import random
import matplotlib.pyplot as plt

n = 10
x = []
y = []
for i in range(100):
    x.append( n*random() )
    y.append( n*random() )

plt.plot(x, y, 'o', color='red', linestyle='None')
plt.show()
