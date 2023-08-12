import random  # Import the random module to generate random numbers

RANDOM_SEED = 12345  # Seed value for random number generation

def main():
    week = 1  # Unused variable, can be removed
    t_values = [0] * 10  # Initialize a list 't_values' with 10 elements, all initialized to 0
    occurrence_count = 0  # Initialize the count of occurrences to 0
    kont_counter = 0   # Initialize another counter to 0
    current_time = 0  # Initialize the clock time to 0
    run_limit = 20000  # Set the maximum run time
    cost_present_policy = 0   # Initialize the cost for the present policy to 0
    cost_proposed_policy = 0   # Initialize the cost for the proposed policy to 0

    random.seed(RANDOM_SEED)  # Seed the random number generator for reproducibility

    # Present policy: Generate and print random numbers for each T value
    for i in range(1, 5):
        random_value = random.random()  # Generate a random number between 0 and 1
        random_value = round(random_value, 6)      # Round the random number to 6 decimal places
        t_values[i] = int(1000 + random_value * 1000)  # Map the random number to a range between 1000 and 2000
        print(f"{t_values[i]:>8}", end=" ")  # Print the value right-aligned in a field width of 8

    # Print a header for the table
    print("\n {:>5} {:>5} {:>5} {:>5} {:>5} {:>5}".format("CLOCK", "T1", "T2", "T3", "T4", "COUNT"))

    # Simulation loop: While the clock time is within the run limit
    while current_time <= run_limit:
        # Print the current clock time and T values
        print(f"\n {current_time:>5} {t_values[1]:>5} {t_values[2]:>5} {t_values[3]:>5} {t_values[4]:>5} {occurrence_count:>5}")

        # Find the smallest T value and its index
        smallest_value = 999999
        smallest_index = 0
        for i in range(1, 5):
            if t_values[i] < smallest_value:
                smallest_value = t_values[i]
                smallest_index = i

        # Subtract the smallest value from all T values
        for i in range(1, 5):
            t_values[i] -= smallest_value

        # Generate a new random number and update the T value with the smallest index
        random_value = random.random()
        random_value = round(random_value, 6)
        t_values[smallest_index] = int(1000 + random_value * 1000)

        # Update the clock time and increment the occurrence count
        current_time += smallest_value
        occurrence_count += 1

    # Proposed policy simulation loop: Reset counters and seed for a new simulation
    current_time = 0
    kont_counter = 0
    random.seed(RANDOM_SEED)

    # Print a header for the proposed policy table
    print("\n {:>5} {:>5} {:>5} {:>5} {:>5} {:>5}".format("CLOCK", "T1", "T2", "T3", "T4", "KONT"))

    # Similar simulation loop for the proposed policy
    while current_time <= run_limit:
        # Generate new random numbers for each T value
        for i in range(1, 5):
            random_value = random.random()
            random_value = round(random_value, 6)
            t_values[i] = int(1000 + random_value * 1000)

        # Print the current clock time and T values
        print(f"\n {current_time:>5} {t_values[1]:>5} {t_values[2]:>5} {t_values[3]:>5} {t_values[4]:>5} {kont_counter:>5}")

        # Find the smallest T value
        smallest_value = 999999
        for i in range(1, 5):
            if t_values[i] < smallest_value:
                smallest_value = t_values[i]

        # Update the clock time and increment the kont counter
        current_time += smallest_value
        kont_counter += 1

    # Calculate costs for both policies
    cost_present_policy = occurrence_count * (200 + 100)
    cost_proposed_policy = kont_counter * 2 * 200 + kont_counter * 4 * 100

    # Print the calculated costs for both policies
    print(f"\nCost Present policy  = {cost_present_policy}\nCost proposed policy = {cost_proposed_policy}")

if __name__ == "__main__":
    main()
