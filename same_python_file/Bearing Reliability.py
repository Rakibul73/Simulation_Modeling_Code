import math
import random
import matplotlib.pyplot as plt
life = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]
probability = [0.10, .14, .24, .14, .12, .10, .06, .05, .03, 0.02]
probability = [int(i * 100) for i in probability]
c_probability = [probability[0]]
i = 1
while i < len(probability):
    c_probability.append(c_probability[i - 1] + probability[i])
    i += 1

delay = [4, 6, 8]
delay_probability = [0.3, 0.6, 0.1]
delay_probability = [int(i * 10) for i in delay_probability]
c_delay_pro = [delay_probability[0]]
i = 1
while i < len(delay_probability):
    c_delay_pro.append(c_delay_pro[i - 1] + delay_probability[i])
    i += 1
def clock():
    x = random.randint(1, 100)
    if x <= c_probability[0]:
        return life[0]
    elif x <= c_probability[1]:
        return life[1]
    elif x <= c_probability[2]:
        return life[2]
    elif x <= c_probability[3]:
        return life[3]
    elif x <= c_probability[4]:
        return life[4]
    elif x <= c_probability[5]:
        return life[5]
    elif x <= c_probability[6]:
        return life[6]
    elif x <= c_probability[7]:
        return life[7]
    elif x <= c_probability[8]:
        return life[8]
    else:
        return life[9]


def late():
    x = random.randint(1, 10)
    if x <= c_delay_pro[0]:
        return delay[0]
    elif x <= c_delay_pro[1]:
        return delay[1]
    else:
        return delay[2]
bearing1_life = []
bearing2_life = []
bearing3_life = []

lf = 0
while lf < 20000:
    i = clock()
    lf += i
    bearing1_life.append(i)
lf = 0
while lf < 20000:
    i = clock()
    lf += i
    bearing2_life.append(i)
lf = 0
while lf < 20000:
    i = clock()
    lf += i
    bearing3_life.append(i)

print(bearing1_life)
print(bearing2_life)
print(bearing3_life)

bearing_life_count = [len(bearing1_life), len(bearing2_life), len(bearing3_life)]

maxlen = max(bearing_life_count)
two_down = 0
three_down = 0
try:
    for i in range(maxlen):
        if (bearing1_life[i] == bearing2_life[i] == bearing3_life[i]):
            three_down += 1
except:
    pass

try:
    for i in range(maxlen):
        if (bearing1_life[i] == bearing2_life[i] or bearing2_life[i] == bearing3_life[i] or bearing3_life[i] ==
                bearing1_life[i]):
            two_down += 1
except:
    pass



total_cost = 0
total_bearing_cost = 0
total_delay_cost = 0
total_repair_cost = 0

num_of_bearing = sum(bearing_life_count)
total_bearing_cost = num_of_bearing * 20

mechanic_delay = []
num_of_mechanic_call = num_of_bearing-two_down-(three_down*2)
for i in range(num_of_mechanic_call):
    x = late()
    mechanic_delay.append(x)
total_delay_cost = sum(mechanic_delay)*5

time_needed = (num_of_bearing*20) - (two_down*10) - (three_down*20)
total_repair_cost = (time_needed/60) * 25

total_cost = total_bearing_cost+total_delay_cost+total_repair_cost

print(total_cost)

bearing_life = []
mechanic_delay_2 = []
lf = 0

while lf<20000:
    life_of_bearings = [clock(),clock(),clock()]
    x = min(life_of_bearings)
    y = late()
    bearing_life.append(x)
    mechanic_delay_2.append(y)
    lf+=x

total_bearing_cost = len(bearing_life)*20
total_delay_cost = sum(mechanic_delay_2)*5
total_repair_cost = ((len(bearing_life)*40)/60)*25

total_cost_2 = total_bearing_cost+total_delay_cost+total_repair_cost


print("Previous Cost : ",total_cost)
print("New Cost : ",total_cost_2)
print("Saves : ",total_cost-total_cost_2)