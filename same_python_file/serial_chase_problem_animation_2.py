# A chase B , B chase C , C chase D , D chase A

import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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

fig, ax = plt.subplots()
line_a, = ax.plot([], [], label='A')
line_b, = ax.plot([], [], label='B')
line_c, = ax.plot([], [], label='C')
line_d, = ax.plot([], [], label='D')
scat_start_a = ax.scatter([], [], color='red', marker='o', label='Start A')
scat_end_a = ax.scatter([], [], color='green', marker='o', label='End A')
scat_start_b = ax.scatter([], [], color='red', marker='o', label='Start B')
scat_end_b = ax.scatter([], [], color='green', marker='o', label='End B')
scat_start_c = ax.scatter([], [], color='red', marker='o', label='Start C')
scat_end_c = ax.scatter([], [], color='green', marker='o', label='End C')
scat_start_d = ax.scatter([], [], color='red', marker='o', label='Start D')
scat_end_d = ax.scatter([], [], color='green', marker='o', label='End D')

def update(frame):
    global a, b, c, d, time

    # Calculate the distances between the objects
    distance_AB = distance(a, b)
    distance_BC = distance(b, c)
    distance_CD = distance(c, d)
    distance_DA = distance(d, a)

    # Update the positions of the objects
    a = (a[0] + va * delt * (b[0] - a[0]) / distance_AB, a[1] + va * delt * (b[1] - a[1]) / distance_AB)
    b = (b[0] - vb * delt * (b[0] - c[0]) / distance_BC, b[1] + vb * delt * (c[1] - b[1]) / distance_BC)
    c = (c[0] - vc * delt * (c[0] - d[0]) / distance_CD, c[1] - vc * delt * (c[1] - d[1]) / distance_CD)
    d = (d[0] + vd * delt * (a[0] - d[0]) / distance_DA, d[1] + vd * delt * (a[1] - d[1]) / distance_DA)

    # Append the positions to the path lists
    path_a.append(a)
    path_b.append(b)
    path_c.append(c)
    path_d.append(d)

    # Check if any of the objects have been hit
    if distance_AB < 0.005:
        print("A hits B")
        anim.event_source.stop()
    elif distance_BC < 0.005:
        print("B hits C")
        anim.event_source.stop()
    elif distance_CD < 0.005:
        print("C hits D")
        anim.event_source.stop()

    # Increase the time
    time += delt

    # Update the plot data
    line_a.set_data(*zip(*path_a))
    line_b.set_data(*zip(*path_b))
    line_c.set_data(*zip(*path_c))
    line_d.set_data(*zip(*path_d))
    scat_start_a.set_offsets([path_a[0]])
    scat_end_a.set_offsets([path_a[-1]])
    scat_start_b.set_offsets([path_b[0]])
    scat_end_b.set_offsets([path_b[-1]])
    scat_start_c.set_offsets([path_c[0]])
    scat_end_c.set_offsets([path_c[-1]])
    scat_start_d.set_offsets([path_d[0]])
    scat_end_d.set_offsets([path_d[-1]])

    return line_a, line_b, line_c, line_d, scat_start_a, scat_end_a, scat_start_b, scat_end_b, scat_start_c, scat_end_c, scat_start_d, scat_end_d

# Set the axis limits
ax.set_xlim(0, 40)
ax.set_ylim(0, 40)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Object Paths')
ax.legend()
ax.grid(True)

# Create the animation
anim = FuncAnimation(fig, update, frames=range(0, 5000), interval=1, blit=True)

# Display the animation
plt.show()
