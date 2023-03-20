
# Bearing Life(Hours)
bearing_life = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]
# Bearing Life(Hours) - Probability
bearing_probabilities = [0.10, 0.14, 0.24, 0.14, 0.12, 0.10, 0.06, 0.05, 0.03, 0.02]

# calculate cumulative probabilities
cumulative_probabilities = [bearing_probabilities[0]]
for i in range(1, len(bearing_probabilities)):
    cumulative_probabilities.append(cumulative_probabilities[i-1] + bearing_probabilities[i])

# generate random digit assignments
bearing_random_digits = []
count = 0
for i in range(len(bearing_probabilities)):
    bearing_random_digits.append([])
    for j in range(int(bearing_probabilities[i]*100)): 
        bearing_random_digits[i].append(count)
        count += 1
        

# for i in range(len(cumulative_probabilities)):
#     print(f"{cumulative_probabilities[i]:.2f}")

# delay Life(minutes)
delay_life = [4 , 6 , 8]
# delay Life(minutes) - Probability
delay_probabilities = [0.3 , 0.6 , 0.1]

# calculate cumulative probabilities
cumulative_probabilities = [delay_probabilities[0]]
for i in range(1, len(delay_probabilities)):
    cumulative_probabilities.append(cumulative_probabilities[i-1] + delay_probabilities[i])

# generate random digit assignments
delay_random_digits = []
count = 0
for i in range(len(delay_probabilities)):
    delay_random_digits.append([])
    for j in range(int(delay_probabilities[i]*10)): 
        delay_random_digits[i].append(count)
        count += 1



# for i in range(len(cumulative_probabilities)):
#     print(f"{cumulative_probabilities[i]:.2f}")

# delay_random_digits

import random

# for bearing 1
total_hours_of_operation = 30000
total_clock_hour = 0
total_change = 0    # how many bearing have to change
bearing_1 = []
bearing_1_delay = []

while total_hours_of_operation > total_clock_hour:
    total_change += 1
    bearing_random_num = random.randint(0 , 99)
    delay_random_num = random.randint(0 , 9)
    current_clock = 0
    current_delay = 0

    # find bearing clock from generated random num
    for i in range(len(bearing_random_digits)):
        if bearing_random_num in bearing_random_digits[i]:
            current_clock = bearing_life[i]
            break

    bearing_1.append(current_clock)
    total_clock_hour += current_clock


    # find delay from generated random num 
    for i in range(len(delay_random_digits)):
        if delay_random_num in delay_random_digits[i]:
            current_delay = delay_life[i]
            break


    bearing_1_delay.append(current_delay)


import random

# for bearing 2
total_hours_of_operation = 30000
total_clock_hour = 0
bearing_2 = []
bearing_2_delay = []

while total_hours_of_operation > total_clock_hour:
    total_change += 1
    bearing_random_num = random.randint(0 , 99)
    delay_random_num = random.randint(0 , 9)
    current_clock = 0
    current_delay = 0

    # find bearing clock from generated random num
    for i in range(len(bearing_random_digits)):
        if bearing_random_num in bearing_random_digits[i]:
            current_clock = bearing_life[i]
            break

    bearing_2.append(current_clock)
    total_clock_hour += current_clock


    # find delay from generated random num 
    for i in range(len(delay_random_digits)):
        if delay_random_num in delay_random_digits[i]:
            current_delay = delay_life[i]
            break


    bearing_2_delay.append(current_delay)


import random

# for bearing 3
total_hours_of_operation = 30000
total_clock_hour = 0
bearing_3 = []
bearing_3_delay = []

while total_hours_of_operation > total_clock_hour:
    total_change += 1
    bearing_random_num = random.randint(0 , 99)
    delay_random_num = random.randint(0 , 9)
    current_clock = 0
    current_delay = 0

    # find bearing clock from generated random num
    for i in range(len(bearing_random_digits)):
        if bearing_random_num in bearing_random_digits[i]:
            current_clock = bearing_life[i]
            break

    bearing_3.append(current_clock)
    total_clock_hour += current_clock


    # find delay from generated random num 
    for i in range(len(delay_random_digits)):
        if delay_random_num in delay_random_digits[i]:
            current_delay = delay_life[i]
            break


    bearing_3_delay.append(current_delay)



maxlen = max( len(bearing_2) , len(bearing_1) , len(bearing_3)  )
two_down = 0
three_down = 0
try:
    for i in range(maxlen):
        if (bearing_1[i] == bearing_2[i] == bearing_3[i]):
            three_down += 1
            max_delay = max(bearing_3_delay[i] , bearing_2_delay[i] , bearing_1_delay[i])
            if bearing_3_delay[i] != max_delay:
                bearing_3_delay[i] = 0
            if bearing_2_delay[i] != max_delay:
                bearing_2_delay[i] = 0
            if bearing_1_delay[i] != max_delay:
                bearing_1_delay[i] = 0
        elif bearing_1[i] == bearing_2[i]:
            two_down += 1
            if bearing_1_delay[i] < bearing_2_delay[i]:
                bearing_1_delay[i] = 0
            else:
                bearing_2_delay[i] = 0
        elif bearing_3[i] == bearing_2[i]:
            two_down += 1
            if bearing_3_delay[i] < bearing_2_delay[i]:
                bearing_3_delay[i] = 0
            else:
                bearing_2_delay[i] = 0
        elif bearing_1[i] == bearing_3[i]:
            two_down += 1
            if bearing_1_delay[i] < bearing_3_delay[i]:
                bearing_1_delay[i] = 0
            else:
                bearing_3_delay[i] = 0




except:
    pass


# print(two_down , three_down)
# print("\n")
# print(bearing_1)
# print(bearing_2)
# print(bearing_3)
# print("\n")
# print(bearing_1_delay)
# print(bearing_2_delay)
# print(bearing_3_delay)


# 20 minutes to change one bearing
# Downtime of the machining center costs Rs. 5 per minute
# direct on job cost of the repairman is Rs. 25 per hour 
# at a time cost of one bearing is Rs. 20.
# at a time cost of two bearing is Rs. 30.
# at a time cost of three bearing is Rs. 40.

one_bearing_change_time_minutes = 20
two_bearing_change_time_minutes = 30
three_bearing_change_time_minutes = 40
cost_of_downtime_per_minutes = 5
cost_of_repairman_per_hour = 25
cost_of_one_bearing = 20

total_repairman_delay_time = sum(bearing_1_delay) + sum(bearing_2_delay) + sum(bearing_3_delay)
print("Total repairman delay time =" , total_repairman_delay_time , "minutes")
time_spent_in_bearing_replacement = (total_change * one_bearing_change_time_minutes) - (two_down * (two_bearing_change_time_minutes - one_bearing_change_time_minutes)) - (three_down * (three_bearing_change_time_minutes - one_bearing_change_time_minutes))
print("Time spent in bearing replacement =", time_spent_in_bearing_replacement , "minutes")
total_downtime = total_repairman_delay_time + time_spent_in_bearing_replacement
print("Total downtime =" , total_downtime , "minutes")

cost_of_downtime = cost_of_downtime_per_minutes*total_downtime
print("Cost of downtime = Rs.",  cost_of_downtime)
cost_of_repairman = time_spent_in_bearing_replacement*cost_of_repairman_per_hour/60
print("Cost of repairman = Rs.",  cost_of_repairman)

print("\n")
print("Total bearing replaced =", total_change)
cost_of_bearing = cost_of_one_bearing*total_change
print("Cost of bearing = Rs.",  cost_of_bearing)

print("\n")
print("Total estimated cost = Rs.",  cost_of_repairman+cost_of_bearing+cost_of_downtime)