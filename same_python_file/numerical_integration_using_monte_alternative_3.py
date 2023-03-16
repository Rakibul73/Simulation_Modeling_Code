# https://youtu.be/WAf0rqwAvgg

from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

a = 2
b = 5 #limits of integration
N = 10000
# a thika b er modde random num dey.. N da

def func(x):
    return x**3

# exact true value
x = sy.Symbol("x")
e = sy.integrate(func(x), (x, a, b))



xrand = random.uniform(a, b , N)



integral = 0.0

for i in range(N):
    integral += func(xrand[i])

answer = (b-a)/float(N)*integral
print("simulated integral value = " , answer)
print("Actual integral value = " , float(e))
