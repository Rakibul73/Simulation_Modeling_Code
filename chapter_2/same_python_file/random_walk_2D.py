# https://www.codingem.com/random-walk-in-python/

import numpy as np
import matplotlib.pyplot as plt
import random

def randomwalk2D(n):
    # [0, 0, 0, ... ,0]
    x = np.zeros(n)
    y = np.zeros(n)

    # jodi sob dike jawar probablity same hoy
    directions = ["UP", "DOWN", "LEFT", "RIGHT"]
    for i in range(1, n):
        # Pick a direction at random
        step = random.choice(directions)
        
        # Move the object according to the direction
        if step == "RIGHT":
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
        elif step == "LEFT":
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
        elif step == "UP":
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1
        elif step == "DOWN":
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1
    
    # Return all the x and y positions of the object
    return x, y

x_data, y_data = randomwalk2D(1000)

plt.title("2D Random Walk in Python")
plt.plot(x_data, y_data)
plt.show()