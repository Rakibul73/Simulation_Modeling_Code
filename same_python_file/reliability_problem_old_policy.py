
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
total_delay_minutes = 0
total_change = 0    # how many bearing have to change

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

    total_clock_hour += current_clock


    # find delay from generated random num 
    for i in range(len(delay_random_digits)):
        if delay_random_num in delay_random_digits[i]:
            current_delay = delay_life[j]
            break


    total_delay_minutes += current_delay


import random

# for bearing 2
total_hours_of_operation = 30000
total_clock_hour = 0


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

    total_clock_hour += current_clock


    # find delay from generated random num 
    for i in range(len(delay_random_digits)):
        if delay_random_num in delay_random_digits[i]:
            current_delay = delay_life[j]
            break


    total_delay_minutes += current_delay


import random

# for bearing 3
total_hours_of_operation = 30000
total_clock_hour = 0


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

    total_clock_hour += current_clock


    # find delay from generated random num 
    for i in range(len(delay_random_digits)):
        if delay_random_num in delay_random_digits[i]:
            current_delay = delay_life[j]
            break


    total_delay_minutes += current_delay



# 20 minutes to change one bearing
# Downtime of the machining center costs Rs. 5 per minute
# direct on job cost of the repairman is Rs. 25 per hour 
# cost of a bearing is Rs. 20.

one_bearing_change_time_minutes = 20
cost_of_downtime_per_minutes = 5
cost_of_repairman_per_hour = 25
cost_of_one_bearing = 20

print("Total repairman delay time =" , total_delay_minutes , "minutes")
print("Time spent in bearing replacement =", total_change*one_bearing_change_time_minutes , "minutes")
print("Total downtime =" , total_delay_minutes+(total_change*one_bearing_change_time_minutes) , "minutes")

cost_of_downtime = cost_of_downtime_per_minutes*(total_delay_minutes+(total_change*one_bearing_change_time_minutes))
print("Cost of downtime = Rs.",  cost_of_downtime)
cost_of_repairman = total_change*one_bearing_change_time_minutes*cost_of_repairman_per_hour/60
print("Cost of repairman = Rs.",  cost_of_repairman)
print("\n")
print("Total bearing replaced =", total_change)
cost_of_bearing = cost_of_one_bearing*total_change
print("Cost of bearing = Rs.",  cost_of_bearing)
print("\n")


print("Total estimated cost = Rs.",  cost_of_repairman+cost_of_bearing+cost_of_downtime)