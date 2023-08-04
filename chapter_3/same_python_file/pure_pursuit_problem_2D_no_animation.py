import math

time_limit = 12.0

fighter_x = [0] * 16
fighter_y = [0] * 16

dist = 0
s = 20.0  # fighter speed = s km/min
fighter_x[0] = 0
fighter_y[0] = 50.0
bomber_x = [100, 110, 120, 129, 140, 149, 158, 168, 179, 188, 198, 209, 219, 226, 234, 240]
bomber_y = [0, 3, 6, 10, 15, 20, 26, 32, 37, 34, 30, 27, 23, 19, 16, 14]
firing_range =  10 # (km) firing range of the fighter

# checks if the bomber is moving too fast for the fighter to catch up
for i in range(len(bomber_x) - 1):
    distance_between_bomber_positions = math.sqrt((bomber_x[i+1] - bomber_x[i])**2 + (bomber_y[i+1] - bomber_y[i])**2)
    time_between_bomber_positions = distance_between_bomber_positions / s
    if time_between_bomber_positions > time_limit:
        print(f"Error: Bomber moves too fast for fighter to catch up. Time between positions {i} and {i+1} is {time_between_bomber_positions:.2f} minutes.")
        exit()


for t in range(int(time_limit)):
    dist = math.sqrt((bomber_y[t]-fighter_y[t])**2 + (bomber_x[t]-fighter_x[t])**2)
    print(f"\n{t}, {dist}")
    if t > time_limit:
        print("Target escapes")
        exit()
    if dist <= firing_range:
        break
    else:
        fighter_x[t+1] = fighter_x[t] + s * ((bomber_x[t] - fighter_x[t])/dist)
        fighter_y[t+1] = fighter_y[t] + s * ((bomber_y[t] - fighter_y[t])/dist)

print(f"\nPursuit ends, shot at {t} minutes and at {dist:.2f} km/s.")
