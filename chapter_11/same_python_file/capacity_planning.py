import random

# Define the cumulative frequency distribution of processing times for orders
cumulative_frequency = [0.0, 0.05, 0.11, 0.21, 0.35, 0.51, 0.67, 0.80, 0.90, 0.97, 1.00]

# Initialize variables
number_of_orders = 0      # Number of orders
number_of_days = 0        # A variable for days
simulation_days = 0       # Days for which simulation is to be run (5000)

random_number, processing_time, total_processing_time, cumulative_hours, machine_capacity, idle_capacity, waiting_time, cumulative_idle_capacity, cumulative_waiting_time = 0.0, 0.0, 0.0, 0.0, 100.0, 0.0, 0.0, 0.0, 0.0
total_cost, cost_per_idle_hour, cost_per_waiting_hour = 0.0, 100.0, 25.0
machine_capacity = 100.0

# Prompt the user to input the number of days for simulation
simulation_days = int(input("\n Enter run: "))

# Print the costs per hour for idle capacity and waiting orders
print("\n Idle capacity cost =", cost_per_idle_hour, "per hour.")
print(" Waiting time cost =", cost_per_waiting_hour, "per hour")

# Loop through different machine capacities from 100 to 200, incrementing by 10
while machine_capacity <= 200:
    cumulative_hours, cumulative_idle_capacity, cumulative_waiting_time = 0.0, 0.0, 0.0
    total_processing_time = 0.0

    # Loop through each day in the simulation
    for number_of_days in range(1, simulation_days + 1):
        # Generate a random number to determine the number of orders for the day
        random_number = random.random()
        for i in range(10):
            j = i + 1
            # Assign the number of orders based on the random number and range
            if random_number > float(i) / 10 and random_number <= float(j) / 10:
                number_of_orders = j

        k = number_of_orders
        
        # Generate machining hours for each order
        for j in range(1, k + 1):
            random_number = random.random()
            # Determine processing time based on the cumulative frequency distribution
            for i in range(10):
                if random_number > cumulative_frequency[i] and random_number <= cumulative_frequency[i + 1]:
                    processing_time = i * 5 + random_number * 5
                    # print("\n", random_number, processing_time)  # Print debugging information
            total_processing_time += processing_time
        
        # Determine if the capacity is underutilized or if there are waiting orders
        if machine_capacity >= total_processing_time:
            idle_capacity = machine_capacity - total_processing_time
            cumulative_idle_capacity += idle_capacity
        else:
            waiting_time = total_processing_time - machine_capacity
            cumulative_waiting_time += waiting_time
        cumulative_hours += total_processing_time
        
        # Reset variables for the next iteration
        total_processing_time, idle_capacity, waiting_time = waiting_time, 0.0, 0.0
    
    # Print simulation results for the current machine capacity
    total_cost = (cumulative_idle_capacity * cost_per_idle_hour) + (cumulative_waiting_time * cost_per_waiting_hour)
    print("\n Capacity =", machine_capacity, "Total cost =", total_cost, "Cost per day =", total_cost / simulation_days)
    machine_capacity += 10  # Increment machine capacity for the next iteration
    print()
