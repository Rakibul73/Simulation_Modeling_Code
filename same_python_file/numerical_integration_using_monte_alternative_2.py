import numpy as np
import matplotlib.pyplot as plt
# https://youtu.be/EnsWVUjpqDE

a = 2
b = 5
n = 10000

x = np.linspace(a, b , n)
y = x**3

plt.title("$f(x) = x^3$")
plt.plot(x, y)

def f(x):
    return (x**3)


X = np.random.uniform(a, b , n)
Y = f(X)*(b-a)

ans = np.sum(Y)/n
print(ans)

