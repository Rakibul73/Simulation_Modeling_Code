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

def randomwalk2D(n):
    n += 1
    x = np.zeros(n)
    y = np.zeros(n)

    for i in range(1, n):
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

        # Move the object according to the direction
        if direction == "forward":
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1
        elif direction == "backward":
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1
        elif direction == "left":
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
        elif direction == "right":
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]

    return x, y

x_data, y_data = randomwalk2D(50)



# create a scatter plot with red points
plt.scatter(x_data, y_data, color='green')
# create a line plot with blue lines connecting the points
plt.plot(x_data, y_data, color='blue')
# add the first point as a cyan point
plt.scatter(x_data[0], y_data[0], color='cyan')
# add the last point as a pink point
plt.scatter(x_data[-1], y_data[-1], color='red')
# set the x-tick and y-tick locations and labels to use integers
plt.xticks(np.arange(int(min(x_data)), int(max(x_data))+1, 1))
plt.yticks(np.arange(int(min(y_data)), int(max(y_data))+1, 1))
plt.title('green Points with Blue Line, Cyan First Point, and red Last Point')
plt.show()