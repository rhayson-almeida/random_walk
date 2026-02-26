import numpy as np
from numpy import random
import matplotlib.pyplot as plt

n_steps = 1000

x= np.zeros(n_steps)
y= np.zeros(n_steps)

for i in range(1,n_steps):
    x_move = random.uniform(0,1)
    y_move = random.uniform(0,1)
    if x_move < 0.5:
        step = -1       # move to left
    else:
        step =1         # move to right
    x[i] = x[i-1] + step

    if y_move < 0.5:
        step = -1
    else:
        step = 1
    y[i] = y[i-1] + step

#steps = np.arange(0, n_steps, 1)
plt.plot(x, y)
plt.xlabel('x_position')
plt.ylabel('y_position')
plt.show()
