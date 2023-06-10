import math

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

print("   t           A                B                C               D")
print("--------------------------------------------------------------------------")

while True:
    # Calculate the distances between the objects
    distance_AB = distance(a, b)
    distance_BC = distance(b, c)
    distance_CD = distance(c, d)

    # Update the positions of the objects
    a = (a[0] + va * delt * (b[0] - a[0]) / distance_AB, a[1] + va * delt * (b[1] - a[1]) / distance_AB)
    b = (b[0] - vb * delt * (b[0] - c[0]) / distance_BC, b[1] + vb * delt * (c[1] - b[1]) / distance_BC)
    c = (c[0] - vc * delt * (c[0] - d[0]) / distance_CD, c[1] - vc * delt * (c[1] - d[1]) / distance_CD)
    d = (d[0] - vd * delt , d[1])
    
    print(f"{time:.3f}   {a[0]:.3f}, {a[1]:.3f}   {b[0]:.3f}, {b[1]:.3f}   {c[0]:.3f}, {c[1]:.3f}   {d[0]:.3f}, {d[1]:.3f}")


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
