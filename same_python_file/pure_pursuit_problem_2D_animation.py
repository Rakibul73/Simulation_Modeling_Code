import math
import time
import matplotlib.pyplot as plt

time_limit = 12 # minutes

fighter_x = [0] * 16
fighter_y = [0] * 16

dist = 0
s = 10.0  # fighter speed = s km/min
fighter_x[0] = 0
fighter_y[0] = 50.0
bomber_x = [100, 110, 120, 129, 140, 149, 158, 168, 179, 188, 198, 209, 219, 226, 234, 240]
bomber_y = [0, 3, 6, 10, 15, 20, 26, 32, 37, 34, 30, 27, 23, 19, 16, 14]
firing_range =  10 # (km) firing range of the fighter
target_escapes = True

for t in range(int(time_limit+1)):
    plt.plot(bomber_x[t], bomber_y[t], 'r*')
    plt.title('Pure Pursuit Problem')
    plt.plot(fighter_x[t], fighter_y[t], 'g*')

    dist = math.sqrt((bomber_y[t]-fighter_y[t])**2 + (bomber_x[t]-fighter_x[t])**2)
    print(f"\n{t}, {dist}")

    if dist <= firing_range:
        print(f"\nPursuit ends, shot at {t} minutes and at {dist:.2f} km/s.")
        target_escapes = False
        break
    
    else:
        fighter_x[t+1] = fighter_x[t] + s * ((bomber_x[t] - fighter_x[t])/dist)
        fighter_y[t+1] = fighter_y[t] + s * ((bomber_y[t] - fighter_y[t])/dist)
    plt.draw()
    plt.pause(1)
    time.sleep(1)

if target_escapes:
    print("\nTarget Escapes")
plt.show()
