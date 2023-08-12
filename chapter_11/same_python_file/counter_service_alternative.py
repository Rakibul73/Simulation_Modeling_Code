import random

# Seed for random number generation
RANDOM_SEED = 12345

def main():
    # Define the number of interarrival values, service values, and servers
    num_interarrival_values = 6
    num_service_values = 5
    num_servers = 4
    
    # Define cumulative probabilities and arrays for interarrival and service times
    cumulative_prob_interarrival = [0, 0.05, 0.4, 0.65, 0.80, 0.90, 0.97, 1.0]
    interarrival_times = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    cumulative_prob_service = [0, 0.05, 0.3, 0.65, 0.85, 1, 0]
    service_times = [1, 2, 3, 4, 5]
    
    # Initialize a list to store service ending times for each server
    service_ending_times = [0.0] * 10
    
    # Get user input for the number of runs
    num_runs = int(input("Enter the value of num_runs: "))

    # Loop through different numbers of servers
    for num_bearers in range(2, num_servers + 1):
        # Print header for the current number of servers
        print("\nRun Length\tAverage Waiting time for S={}".format(num_bearers))
        
        # Loop through different run lengths
        for run_length in range(50, 501, 100):
            # Initialize the variable to store the average waiting time
            avg_waiting_time = 0.0
            
            # Run the simulation for the prescribed number of runs
            for iteration in range(1, num_runs + 1):
                # Set the random seed for reproducibility
                random.seed(RANDOM_SEED)
                
                # Initialize the variables for the current simulation run
                arrival_counter = 0
                next_arrival_time = 0.0
                cumulative_waiting_time = 0.0
                
                # Initialize the service ending times for each server
                for i in range(1, num_bearers + 1):
                    service_ending_times[i] = 0.0

                # Run the simulation for the prescribed length of run
                for arrival_counter in range(1, run_length + 1):
                    # Generate the interarrival and service times for the new arrival
                    random_value_old = random.random()
                    random_value = round(random_value_old, 6)
                    for i in range(num_interarrival_values + 1):
                        if cumulative_prob_interarrival[i] < random_value <= cumulative_prob_interarrival[i + 1]:
                            interarrival_time = interarrival_times[i]
                    random_value_old = random.random()
                    random_value = round(random_value_old, 6)
                    for i in range(num_service_values + 1):
                        if cumulative_prob_service[i] < random_value <= cumulative_prob_service[i + 1]:
                            service_time = service_times[i]

                    # Update the next arrival time
                    next_arrival_time += interarrival_time

                    # Determine the earliest service ending time and bearer, then update the statistics
                    min_ending_time = 99.9
                    waiting_time = 0
                    for i in range(1, num_bearers + 1):
                        if service_ending_times[i] <= min_ending_time:
                            min_ending_time = service_ending_times[i]
                            chosen_bearer = i
                    if next_arrival_time <= min_ending_time:
                        service_ending_times[chosen_bearer] = min_ending_time + service_time
                        waiting_time = min_ending_time - next_arrival_time
                    else:
                        service_ending_times[chosen_bearer] = next_arrival_time + service_time

                    # Accumulate waiting time
                    cumulative_waiting_time += waiting_time

                # Calculate average waiting time for the current run and accumulate it
                avg_waiting_time += cumulative_waiting_time / run_length

            # Print the average waiting time for the current run length and number of servers
            print("{}\t\t{:8.2f}".format(run_length, avg_waiting_time / num_runs))

if __name__ == "__main__":
    main()
