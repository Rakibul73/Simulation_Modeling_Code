import numpy as np
import matplotlib.pyplot as plt
import random
# Random walk - Probability forward , backward , left , right = 40% 10% 25% 25%
random_walk_probabilities = [0.4 , 0.1 , 0.25 , 0.25]

# calculate cumulative probabilities
cumulative_probabilities = [random_walk_probabilities[0]]
for i in range(1, len(random_walk_probabilities)):
    cumulative_probabilities.append(cumulative_probabilities[i-1] + random_walk_probabilities[i])

# generate random digit assignments
random_walk_random_digits = []
count = 0
for i in range(len(random_walk_probabilities)):
    random_walk_random_digits.append([])
    for j in range(int(random_walk_probabilities[i]*100)): 
        random_walk_random_digits[i].append(count)
        count += 1
        

# for i in range(len(cumulative_probabilities)):
#     print(f"{cumulative_probabilities[i]:.2f}")
import random
import math
import matplotlib.pyplot as plt

# set up the distances in the x and y axes
up, down, left, right = 75, 45, 60, 60

# initialize the starting point as (0,0)
x, y = 0, 0

# create empty lists to store the x and y coordinates of the movement
x_list = [x]
y_list = [y]

# generate a random direction and move accordingly
for i in range(50):  # move 50 times
    step = random.randint(0,99)
    global direction
    
    # find direction from generated random num
    for j in range(len(random_walk_random_digits)):
        if step in random_walk_random_digits[j]:
            if j == 0:
                direction = "forward"
            if j == 1:
                direction = "backward"
            if j == 2:
                direction = "left"
            if j == 3:
                direction = "right"
            break
    
    if direction == 'forward':
        y += up
    elif direction == 'backward':
        y -= down
    elif direction == 'left':
        x -= left
    else:
        x += right
    x_list.append(x)
    y_list.append(y)

# calculate the total distance covered
distance = math.sqrt(x**2 + y**2)

# create a scatter plot with green points
plt.scatter(x_list, y_list , color='green')
# create a line plot with blue lines connecting the points
plt.plot(x_list, y_list , color='blue')
# add the first point as a cyan point
plt.scatter(x_list[0], y_list[0], color='cyan')
# add the last point as a pink point
plt.scatter(x_list[-1], y_list[-1], color='red')
plt.title(f"Total Distance Covered: {distance:.2f} cm")
plt.xlabel("X-axis (cm)")
plt.ylabel("Y-axis (cm)")
plt.show()
