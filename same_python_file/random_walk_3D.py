# https://www.codingem.com/random-walk-in-python/

import matplotlib.pyplot as plt
import numpy as np
import random

def randomwalk3D(n):
    x, y, z = np.zeros(n), np.zeros(n), np.zeros(n)

    # jodi sob dike jawar probablity same hoy
    directions = ["UP", "DOWN", "LEFT", "RIGHT", "IN", "OUT"]
    for i in range(1, n):
        step = random.choice(directions)

        if step == "RIGHT":
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
            z[i] = z[i - 1]
        elif step == "LEFT":
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
            z[i] = z[i - 1]
        elif step == "UP":
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1
            z[i] = z[i - 1]
        elif step == "DOWN":
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1
            z[i] = z[i - 1]
        elif step == "IN":
            x[i] = x[i - 1]
            y[i] = y[i - 1]
            z[i] = z[i - 1] - 1
        elif step == "OUT":
            x[i] = x[i - 1]
            y[i] = y[i - 1]
            z[i] = z[i - 1] + 1

    return x, y, z

x_data, y_data, z_data = randomwalk3D(1000)

ax = plt.subplot(1, 1, 1, projection='3d')
ax.plot(x_data, y_data, z_data, alpha=0.9)
ax.scatter(x_data[-1], y_data[-1], z_data[-1])

plt.show()