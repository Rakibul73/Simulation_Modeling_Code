import math

def simulate_projectile(v0, el, k, m, n):
    # Convert the angle of elevation from degrees to radians
    theta = math.radians(el)
    
    # Initialize variables
    x = 0
    y = 0
    g = 9.8  # Acceleration due to gravity
    
    # Set a small time interval for simulation accuracy
    dt = 0.01
    
    # Lists to store the trajectory points
    trajectory_x = [x]
    trajectory_y = [y]
    
    # Perform simulation until the projectile touches the ground
    while y >= 0:
        # Calculate the change in velocity
        dv = -g * math.sin(theta) - (k * math.pow(v0, n) / m)
        
        # Calculate the change in angle
        dtheta = -g * math.cos(theta) / v0
        
        # Calculate the change in position
        dx = v0 * math.cos(theta) * dt
        dy = v0 * math.sin(theta) * dt
        
        # Update velocity, angle, and position
        v0 += dv * dt
        theta += dtheta * dt
        x += dx
        y += dy
        
        # Add the current position to the trajectory
        trajectory_x.append(x)
        trajectory_y.append(y)
    
    return trajectory_x, trajectory_y

# Example usage
v0 = 100  # Initial velocity in m/s
el = 45  # Angle of elevation in degrees
k = 0.1  # Drag coefficient
m = 30  # Mass of the projectile in kg
n = 0.001  # Power of velocity for air resistance

trajectory_x, trajectory_y = simulate_projectile(v0, el, k, m, n)

# Print the trajectory points
for i in range(len(trajectory_x)):
    print(f"Point {i+1}: x = {trajectory_x[i]}, y = {trajectory_y[i]}")
