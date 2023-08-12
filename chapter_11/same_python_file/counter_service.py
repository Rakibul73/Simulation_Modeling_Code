# Import the random module to generate random numbers
import random

# Define the main function to run the simulation
def main():
    # Define parameters for the simulation
    n = 6  # Number of values in the interarrival time array
    m = 5  # Number of values in the service time array
    s = 4  # Number of servers (bearers)
    
    # Initialize lists to store simulation data
    service_ending_times = [0.0] * 10  # List to keep track of service ending times for each server
    cumulative_prob_interarrival = [0, 0.05, 0.4, 0.65, 0.80, 0.90, 0.97, 1.0]  # Array of cumulative probabilities for interarrival times
    interarrival_times = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]  # Array of interarrival times
    cumulative_prob_service = [0, 0.05, 0.3, 0.65, 0.85, 1, 0]  # Array of cumulative probabilities for service times
    service_times = [1, 2, 3, 4, 5]  # Array of service times

    # Get user input for the number of runs
    print("\nEnter the value of run: ")
    run = int(input())

    # Loop through different number of servers
    for num_servers in range(2, s + 1):
        # Set the random seed for reproducibility of results
        random.seed(12345)
        
        # Initialize variables for the simulation
        arrival_counter = 0  # Counter to keep track of the number of arrivals
        next_arrival_time = 0.0  # Simulation clock representing the next arrival time
        cumulative_waiting_time = 0.0  # Cumulative waiting time for all customers

        # Initialize the service ending times for each server
        for i in range(1, num_servers + 1):
            service_ending_times[i] = 0.0

        current_waiting_time = 0.0  # Initialize the waiting time for the current customer

        # Run the simulation for the prescribed number of runs
        for arrival_counter in range(1, run + 1):
            # Generate random numbers for interarrival and service times
            random_value = random.random()
            for i in range(n):
                if random_value > cumulative_prob_interarrival[i] and random_value <= cumulative_prob_interarrival[i + 1]:
                    interarrival_time = interarrival_times[i]
            
            random_value = random.random()
            for i in range(m):
                if random_value > cumulative_prob_service[i] and random_value <= cumulative_prob_service[i + 1]:
                    service_time = service_times[i]

            # Update the simulation clock and calculate waiting time
            next_arrival_time = next_arrival_time + interarrival_time

            # Find the earliest service ending time and corresponding server
            min_val = 99.9
            chosen_server = 1
            for i in range(1, num_servers + 1):
                if service_ending_times[i] <= min_val:
                    min_val = service_ending_times[i]
                    chosen_server = i

            # Assign service ending time for the current customer and update waiting time
            if next_arrival_time <= min_val:
                service_ending_times[chosen_server] = min_val + service_time
                current_waiting_time = min_val - next_arrival_time
            else:
                service_ending_times[chosen_server] = next_arrival_time + service_time

            # Accumulate waiting time for all customers
            cumulative_waiting_time += current_waiting_time

        # Print the simulation results for the current number of servers
        print(f"\nServers = {num_servers} Total arrivals = {arrival_counter} Average Waiting time = {cumulative_waiting_time / run:6.2f}")

# Check if the script is being run as the main program and call the main function
if __name__ == "__main__":
    main()
