import math

amount = 0
initial_inv_level = 0
inv_level = 0
next_event_type = 0
num_events = 0
num_months = 0
num_values_demand = 0
area_holding = 0.0
area_shortage = 0.0
holding_cost = 0.0
incremental_cost = 0.0
maxlag = 0.0
mean_interdemand = 0.0
minlag = 0.0
prob_distrib_demand = [0.0] * 4
setup_cost = 0.0
shortage_cost = 0.0
sim_time = 0.0
time_last_event = 0.0
time_next_event = [0.0] * 5
total_ordering_cost = 0.0


# Constants for random number generation
MODLUS = 2147483647
MULT1 = 24112
MULT2 = 26143
# List of random number generator seeds
zrng = [1, 1973272912, 281629770, 20006270, 1280689831, 2096730329, 1933576050,
        913566091, 246780520, 1363774876, 604901985, 1511192140, 1259851944,
        824064364, 150493284, 242708531, 75253171, 1964472944, 1202299975,
        233217322, 1911216000, 726370533, 403498145, 993232223, 1103205531,
        762430696, 1922803170, 1385516923, 76271663, 413682397, 726466604,
        336157058, 1432650381, 1120463904, 595778810, 877722890, 1046574445,
        68911991, 2088367019, 748545416, 622401386, 2122378830, 640690903,
        1774806513, 2132545692, 2079249579, 78130110, 852776735, 1187867272,
        1351423507, 1645973084, 1997049139, 922510944, 2045512870, 898585771,
        243649545, 1004818771, 773686062, 403188473, 372279877, 1901633463,
        498067494, 2087759558, 493157915, 597104727, 1530940798, 1814496276,
        536444882, 1663153658, 855503735, 67784357, 1432404475, 619691088,
        119025595, 880802310, 176192644, 1116780070, 277854671, 1366580350,
        1142483975, 2026948561, 1053920743, 786262391, 1792203830, 1494667770,
        1923011392, 1433700034, 1244184613, 1147297105, 539712780, 1545929719,
        190641742, 1645390429, 264907697, 620389253, 1502074852, 927711160,
        364849192, 2049576050, 638580085, 547070247]


# Random number generation function (lcgrand) is a random number generator 
# that generates uniform random numbers between 0 and 1.
# It is based on a linear congruential generator and uses a list of seeds (zrng) to generate random numbers.
def lcgrand(stream):
    global zrng
    zi, lowprd, hi31 = zrng[stream], 0, 0
    lowprd = (zi & 65535) * MULT1
    hi31 = (zi >> 16) * MULT1 + (lowprd >> 16)
    zi = ((lowprd & 65535) - MODLUS) + ((hi31 & 32767) << 16) + (hi31 >> 15)
    if zi < 0:
        zi += MODLUS
    lowprd = (zi & 65535) * MULT2
    hi31 = (zi >> 16) * MULT2 + (lowprd >> 16)
    zi = ((lowprd & 65535) - MODLUS) + ((hi31 & 32767) << 16) + (hi31 >> 15)
    if zi < 0:
        zi += MODLUS
    zrng[stream] = zi
    return (zi >> 7 | 1) / 16777216.0


# Random seed setting function (lcgrandst) sets the seed (zset) for a specific stream of the random number generator.
# It changes the value of a seed in the zrng list, which will affect the sequence of random numbers generated.
def lcgrandst(zset, stream):
    global zrng
    zrng[stream] = zset


# Random number getter function (lcgrandgt) retrieves the current seed value for a specific stream of the random number generator.
def lcgrandgt(stream):
    global zrng
    return zrng[stream]



# The expon function generates exponentially distributed random numbers using the inverse transform method.
# It calls the lcgrand function to get a uniform random number and then transforms it to an exponential distribution.
def expon(mean):
    return -mean * math.log(lcgrand(1))


# Function to determine the next event and update simulation time
def timing():
    global next_event_type, sim_time , num_events , time_next_event
    min_time_next_event = 1.0e+29
    next_event_type = 0

    # Find the minimum time for the next event and identify the type of that event
    for i in range(1, num_events + 1):
        if time_next_event[i] < min_time_next_event:
            min_time_next_event = time_next_event[i]
            next_event_type = i

    # If no event is scheduled, terminate the simulation
    if next_event_type == 0:
        print("\nEvent list empty at time", sim_time)
        exit(1)

    # Update the simulation time to the time of the next event
    sim_time = min_time_next_event

def report(smalls, bigs):
    global num_months, area_holding, area_shortage, holding_cost, shortage_cost, total_ordering_cost
    avg_holding_cost = 0.0
    avg_ordering_cost = 0.0
    avg_shortage_cost = 0.0
    
    # Compute and display estimates of desired measures of performance.
    avg_holding_cost = total_ordering_cost / num_months  # Calculate average holding cost per month.
    avg_holding_cost = holding_cost * area_holding / num_months  # Update average holding cost using area_holding.
    avg_shortage_cost = shortage_cost * area_shortage / num_months  # Calculate average shortage cost per month.
    
    # Print the formatted report with various performance metrics.
    print("\n\n({:3d},{:3d}){:15.2f}{:15.2f}{:15.2f}{:15.2f}".format(
        smalls, bigs,
        avg_ordering_cost + avg_holding_cost + avg_shortage_cost,
        avg_ordering_cost, avg_holding_cost, avg_shortage_cost))

def initialize():
    global sim_time, mean_interdemand, num_months, inv_level, time_last_event, total_ordering_cost, area_holding, area_shortage, time_next_event
    
    # Initialize the simulation clock.
    sim_time = 0.0
    
    # Initialize the state variables.
    inv_level = initial_inv_level  # Set initial inventory level.
    time_last_event = 0.0
    
    # Initialize the statistical counters.
    total_ordering_cost = 0.0
    area_holding = 0.0
    area_shortage = 0.0
    
    # Initialize the event list. Since no order is outstanding, the order-arrival event is eliminated from consideration.
    time_next_event[1] = 1.0e+30  # Initialize order-arrival event time to a large value.
    time_next_event[2] = sim_time + expon(mean_interdemand)  # Schedule the first demand event.
    time_next_event[3] = num_months  # Schedule the end of simulation event.
    time_next_event[4] = 0.0  # Schedule the next inventory evaluation event.

def order_arrival():
    global inv_level, time_next_event, amount
    # Increment the inventory level by the amount ordered.
    inv_level += amount
    # Since no order is now outstanding, eliminate the order-arrival event from consideration.
    time_next_event[1] = 1.0e+30

def demand():
    global inv_level, time_next_event, prob_distrib_demand, mean_interdemand, sim_time
    # Decrement the inventory level by a generated demand size.
    inv_level -= random_integer(prob_distrib_demand)
    # Schedule the time of the next demand.
    time_next_event[2] = sim_time + expon(mean_interdemand)


def evaluate(smalls, bigs):
    global inv_level, sim_time, time_next_event, amount, total_ordering_cost, incremental_cost, maxlag, minlag, setup_cost
    # Check whether the inventory level is less than smalls.
    if inv_level < smalls:
        # The inventory level is less than smalls, so place an order for the appropriate amount.
        amount = bigs - inv_level
        total_ordering_cost += setup_cost + incremental_cost * amount
        # Schedule the arrival of the order.
        time_next_event[1] = sim_time + uniform(minlag, maxlag)
    # Regardless of the place-order decision, schedule the next inventory evaluation.
    time_next_event[4] = sim_time + 1.0


def update_time_avg_stats():
    global sim_time, time_last_event, inv_level, area_shortage, area_holding
    # Calculate the time elapsed since the last event occurred.
    time_since_last_event = sim_time - time_last_event
    # Update the time of the last event to the current simulation time.
    time_last_event = sim_time
    
    # Check if there was a shortage (negative inventory).
    if inv_level < 0:
        # Update the area_shortage counter by subtracting the negative inventory level multiplied by the time since the last event.
        area_shortage -= inv_level * time_since_last_event
    # Check if there was holding inventory (positive inventory).
    elif inv_level > 0:
        # Update the area_holding counter by adding the inventory level multiplied by the time since the last event.
        area_holding += inv_level * time_since_last_event


def random_integer(prob_distrib):
    # Generate a random integer according to a given probability distribution.
    u = lcgrand(1)  # Generate a random number between 0 and 1
    i = 1  # Initialize index for the probability distribution
    # Find the appropriate index based on the generated random number and probability distribution
    while u >= prob_distrib[i]:
        i += 1
    return i  # Return the selected index, which represents the generated random integer

def uniform(a, b):
    # Generate a random number from a uniform distribution between 'a' and 'b'.
    return a + lcgrand(1) * (b - a)  # Scale and shift the generated random number




def main():
    global num_events ,prob_distrib_demand , initial_inv_level , num_months , num_policies , \
    num_values_demand , mean_interdemand , setup_cost , incremental_cost , holding_cost , \
    shortage_cost , minlag , maxlag , next_event_type
    num_events = 4
    
    # Read input parameters
    initial_inv_level, num_months, num_policies, num_values_demand, \
    mean_interdemand, setup_cost, incremental_cost, holding_cost, \
    shortage_cost, minlag, maxlag = map(float, input().split())
    
    # Read the demand distribution values
    prob_distrib_demand = [0.0]  # Initialize with 0 at index 0
    prob_distrib_demand.extend(map(float, input().split()))
    
    # Read inventory policy pairs
    print("Enter inventory policy pairs (smalls bigs) for each policy:")
    smalls_arr = []  # Initialize with 0 at index 0
    bigs_arr = []    # Initialize with 0 at index 0
    for _ in range(int(num_policies)):
        smalls, bigs = map(int, input().split())
        smalls_arr.append(smalls)
        bigs_arr.append(bigs)
    
    # Print report heading and input parameters
    print("Single-product inventory system\n")
    print(f"Initial inventory level{'':18}{int(initial_inv_level)} items")
    print(f"Number of demand sizes{'':19}{int(num_values_demand)}")
    print("Distribution function of demand sizes", end=" ")
    for i in range(1, int(num_values_demand) + 1):
        print(f"{prob_distrib_demand[i]:>8.3f}", end="")
    print(f"\nMean interdemand time{'':21}{mean_interdemand:.2f}")
    print(f"Delivery lag range{'':24}{minlag:.2f} to{'':10}{maxlag:.2f} months")
    print(f"Length of the simulation{'':19}{int(num_months)} months")
    print(f"K ={'':9}{setup_cost:.1f} i ={'':7}{incremental_cost:.1f} "
          f"h ={'':7}{holding_cost:.1f} pi ={'':7}{shortage_cost:.1f}")
    print(f"Number of policies{'':23}{int(num_policies)}\n")
    
    
    print("Policy\tAverage total cost\tAverage ordering cost\tAverage holding cost\tAverage shortage cost")
    
    print(num_policies)
    # Run the simulation varying the inventory policy
    for i in range(int(num_policies)):
        # Read the inventory policy, and initialize the simulation.
        smalls = smalls_arr[i]
        bigs = bigs_arr[i]
        initialize()
        next_event_type = 0
        # Run the simulation until it terminates after an end-simulation event (type 3) occurs.
        while next_event_type != 3:
            # Determine the next event.
            timing()
            
            # Update time-average statistical accumulators.
            update_time_avg_stats()
            
            # Invoke the appropriate event function.
            if next_event_type == 1:
                order_arrival()
            elif next_event_type == 2:
                demand()
            elif next_event_type == 4:
                evaluate(smalls , bigs)
            elif next_event_type == 3:
                report(smalls , bigs)

if __name__ == "__main__":
    main()


'''

60 120 9 4 0.10 32.0 3.0 1.0 5.0 0.50 1.0
0.167 0.500 0.833 1.000
20 40
20 60
20 80
20 100
40 60
40 80
40 100
60 80
60 100



'''