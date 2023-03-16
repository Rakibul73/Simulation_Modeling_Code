# https://www.nickmccullum.com/monte-carlo-simulations-python/
import random
import math
n = 100000000
n_inside_circle = 0
for i in  range(0,n):
	x = random.random()
	y = random.random()

	if((x*x+y*y)<=1):
		n_inside_circle += 1
pi = 4*n_inside_circle/n
print(pi)