# A chase B , B chase C , C chase D , D goes straight line in y direction

import math
import matplotlib.pyplot as plt

def distance(a, b):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

# Initialize the Position
a = (10, 10)
b = (30, 10)
c = (30, 30)
d = (10, 30)

# Initialize the velocities
va = 35
vb = 25
vc = 15
vd = 10

# Initialize the time and time increment
time = 0
delt = 0.001

# Create empty lists to store the positions
path_a = [a]
path_b = [b]
path_c = [c]
path_d = [d]

while True:
    # Calculate the distances between the objects
    distance_AB = distance(a, b)
    distance_BC = distance(b, c)
    distance_CD = distance(c, d)

    # Update the positions of the objects
    a = (a[0] + va * delt * (b[0] - a[0]) / distance_AB, a[1] + va * delt * (b[1] - a[1]) / distance_AB)
    b = (b[0] - vb * delt * (b[0] - c[0]) / distance_BC, b[1] + vb * delt * (c[1] - b[1]) / distance_BC)
    c = (c[0] - vc * delt * (c[0] - d[0]) / distance_CD, c[1] - vc * delt * (c[1] - d[1]) / distance_CD)
    d = (d[0] - vd * delt , d[1]) # D goes straight line in y direction

    # Append the positions to the path lists
    path_a.append(a)
    path_b.append(b)
    path_c.append(c)
    path_d.append(d)

    # Check if any of the objects have been hit
    if distance_AB < 0.005:
        print("A hits B")
        break
    elif distance_BC < 0.005:
        print("B hits C")
        break
    elif distance_CD < 0.005:
        print("C hits D")
        break

    # Increase the time
    time += delt

# Extract x and y coordinates from the path lists
path_a_x, path_a_y = zip(*path_a)
path_b_x, path_b_y = zip(*path_b)
path_c_x, path_c_y = zip(*path_c)
path_d_x, path_d_y = zip(*path_d)

# Plot the paths
plt.plot(path_a_x, path_a_y, label='A')
plt.plot(path_b_x, path_b_y, label='B')
plt.plot(path_c_x, path_c_y, label='C')
plt.plot(path_d_x, path_d_y, label='D')
plt.scatter(path_a_x[0], path_a_y[0], color='red', marker='o', label='Start')
plt.scatter(path_a_x[-1], path_a_y[-1], color='green', marker='o', label='End')
plt.scatter(path_b_x[0], path_b_y[0], color='red', marker='o')
plt.scatter(path_b_x[-1], path_b_y[-1], color='green', marker='o')
plt.scatter(path_c_x[0], path_c_y[0], color='red', marker='o')
plt.scatter(path_c_x[-1], path_c_y[-1], color='green', marker='o')
plt.scatter(path_d_x[0], path_d_y[0], color='red', marker='o')
plt.scatter(path_d_x[-1], path_d_y[-1], color='green', marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Object Paths')
plt.legend()
plt.grid(True)
plt.show()
