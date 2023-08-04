import math

def bullet_trajectory():
    # Constants and initial values
    v0 = 350  # Initial velocity in m/s
    angle = 40  # Angle of projection in degrees
    c = -0.00005  # Resistance coefficient
    delt = 0.01  # Time interval for simulation
    g = 9.81  # Acceleration due to gravity
    
    theta = math.radians(angle)  # Convert angle to radians

    # Initialize variables
    x = 0
    y = 0
    t = 0
    range_val = 0
    max_height = 0

    # Simulation loop
    while y >= 0:
        # Calculate changes in velocity, angle, and position
        delv = (-g * math.sin(theta) + c * v0**2) * delt
        dtheta = -g * math.cos(theta) * delt / v0
        delx = v0 * math.cos(theta) * delt
        dely = v0 * math.sin(theta) * delt - 0.5 * g * delt**2

        # Update velocity, angle, and position
        v0 += delv
        theta += dtheta
        x += delx
        y += dely

        # Update range and maximum height
        if y >= 0:
            range_val = x
            max_height = max(max_height, y)

        # Update time of flight
        t += delt

    # Calculate the angle of fall
    angle_of_fall = math.degrees(math.atan(y / x))

    # Print the results
    print("Bullet Trajectory")
    print("-------------------------------")
    print(f"Initial Velocity: {v0} m/s")
    print(f"Angle of Projection: {angle} degrees")
    print(f"Range: {range_val:.2f} meters")
    print(f"Time of Flight: {t:.2f} seconds")
    print(f"Angle of Fall: {angle_of_fall:.2f} degrees")
    print(f"Maximum Height: {max_height:.2f} meters")


bullet_trajectory()
