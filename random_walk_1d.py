import numpy as np
from numpy import random
import matplotlib.pyplot as plt

n_steps = 10

position= np.zeros(n_steps)

for i in range(1,n_steps):
    move = random.uniform(0,1)
    if move < 0.5:
        step = -1       # move to left
    else:
        step =1         # move to right
    position[i] = position[i-1] + step

steps = np.arange(0, n_steps, 1)
plt.plot(steps, position)
plt.xlabel('number of steps')
plt.ylabel('position')
plt.show()
