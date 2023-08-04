# Import the random module to generate random numbers
import random

# Define the main function to run the simulation
def main():
    # Define parameters for the simulation
    n = 6  # Number of values in the at array
    m = 5  # Number of values in the t array
    s = 4  # Number of servers (bearers)
    
    # Initialize lists to store simulation data
    se = [0.0] * 10  # List to keep track of service ending times for each server
    p = [0, 0.05, 0.4, 0.65, 0.80, 0.90, 0.97, 1.0]  # Array of cumulative probabilities for interarrival times
    at = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]  # Array of interarrival times
    f = [0, 0.05, 0.3, 0.65, 0.85, 1, 0]  # Array of cumulative probabilities for service times
    t = [1, 2, 3, 4, 5]  # Array of service times

    # Get user input for the number of runs
    print("\nEnter the value of run: ")
    run = int(input())

    # Loop through different number of servers
    for j in range(2, s + 1):
        # Set the random seed for reproducibility of results
        random.seed(12345)
        
        # Initialize variables for the simulation
        counter = 0  # Counter to keep track of the number of arrivals
        nat = 0.0  # Simulation clock representing the next arrival time
        cwt = 0.0  # Cumulative waiting time for all customers

        # Initialize the service ending times for each server
        for i in range(1, j + 1):
            se[i] = 0.0

        wt = 0.0  # Initialize the waiting time for the current customer

        # Run the simulation for the prescribed number of runs
        for counter in range(1, run + 1):
            # Generate random numbers for interarrival and service times
            r = random.random()
            for i in range(n):
                if r > p[i] and r <= p[i + 1]:
                    iat = at[i]
            
            r = random.random()
            for i in range(m):
                if r > f[i] and r <= f[i + 1]:
                    st = t[i]

            # Update the simulation clock and calculate waiting time
            nat = nat + iat

            # Find the earliest service ending time and corresponding server
            min_val = 99.9
            k = 1
            for i in range(1, j + 1):
                if se[i] <= min_val:
                    min_val = se[i]
                    k = i

            # Assign service ending time for the current customer and update waiting time
            if nat <= min_val:
                se[k] = min_val + st
                wt = min_val - nat
            else:
                se[k] = nat + st

            # Accumulate waiting time for all customers
            cwt += wt

        # Print the simulation results for the current number of servers
        print(f"\nServers = {j} Total arrivals = {counter} Average Waiting time = {cwt / run:6.2f}")

# Check if the script is being run as the main program and call the main function
if __name__ == "__main__":
    main()
