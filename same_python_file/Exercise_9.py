import numpy as np
import matplotlib.pyplot as plt

x = 10 + np.random.uniform(low=-10, high=10, size=200)
y = 10 + np.random.uniform(low=-8, high=8, size=200)

z_a = x * y
plt.hist(z_a , ec="red" ,color='green')
plt.show()
print("Mean of z_a:", np.mean(z_a))

z_b = x / y
plt.hist(z_b , ec="red" ,color='green')
plt.show()
print("Mean of z_b:", np.mean(z_b))
