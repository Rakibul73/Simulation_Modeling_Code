import math

def cannon_range_table():
    # Constants and initial values
    m = 0.1  # Mass of cannon ball in kg
    c = 0.1  # Drag coefficient
    g = 9.81  # Acceleration due to gravity
    
    v0_range = range(100, 1001, 100)  # Range of initial velocities (m/s)
    angle_range = range(5, 91, 5)  # Range of firing angles (degrees)

    print("Range Table")
    print("-------------------------------")
    print("Firing Angle (deg)\tInitial Velocity (m/s)\tRange (m)")
    
    for angle in angle_range:
        for v0 in v0_range:
            # Convert angle to radians
            theta = math.radians(angle)
            
            # Initial values
            x = 0
            y = 0
            t = 0
            
            while y >= 0:
                # Calculate changes in velocity and position
                delv = (-g * math.sin(theta) - (c * v0**2) / m) * t
                delx = v0 * math.cos(theta) * t
                dely = v0 * math.sin(theta) * t - 0.5 * g * t**2
                
                # Update velocity and position
                v0 += delv
                x += delx
                y += dely
                t += 0.01
                
            # Print the firing angle, initial velocity, and range
            print(f"{angle}\t\t\t{v0}\t\t\t\t{x:.2f}")

cannon_range_table()
