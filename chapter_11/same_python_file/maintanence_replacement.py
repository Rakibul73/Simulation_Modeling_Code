import random  # Import the random module to generate random numbers

SEED = 12345  # Seed value for random number generation

def main():
    week = 1  # Unused variable, can be removed
    t = [0] * 10  # Initialize a list 't' with 10 elements, all initialized to 0
    count = 0  # Initialize the count of occurrences to 0
    kont = 0   # Initialize another counter to 0
    clock = 0  # Initialize the clock time to 0
    run = 20000  # Set the maximum run time
    cost1 = 0   # Initialize the cost1 to 0
    cost2 = 0   # Initialize the cost2 to 0

    random.seed(SEED)  # Seed the random number generator for reproducibility

    # Present policy: Generate and print random numbers for each T value
    for i in range(1, 5):
        x = random.random()  # Generate a random number between 0 and 1
        x = round(x, 6)      # Round the random number to 6 decimal places
        t[i] = int(1000 + x * 1000)  # Map the random number to a range between 1000 and 2000
        print(f"{t[i]:>8}", end=" ")  # Print the value right-aligned in a field width of 8

    # Print a header for the table
    print("\n {:>5} {:>5} {:>5} {:>5} {:>5} {:>5}".format("CLOCK", "T1", "T2", "T3", "T4", "COUNT"))

    # Simulation loop: While the clock time is within the run limit
    while clock <= run:
        # Print the current clock time and T values
        print(f"\n {clock:>5} {t[1]:>5} {t[2]:>5} {t[3]:>5} {t[4]:>5} {count:>5}")

        # Find the smallest T value and its index
        small = 999999
        jj = 0
        for i in range(1, 5):
            if t[i] < small:
                small = t[i]
                jj = i

        # Subtract the smallest value from all T values
        for i in range(1, 5):
            t[i] -= small

        # Generate a new random number and update the T value with the smallest index
        x = random.random()
        x = round(x, 6)
        t[jj] = int(1000 + x * 1000)

        # Update the clock time and increment the count
        clock += small
        count += 1

    # Proposed policy simulation loop: Reset counters and seed for a new simulation
    clock = 0
    kont = 0
    random.seed(SEED)

    # Print a header for the proposed policy table
    print("\n {:>5} {:>5} {:>5} {:>5} {:>5} {:>5}".format("CLOCK", "T1", "T2", "T3", "T4", "KONT"))

    # Similar simulation loop for the proposed policy
    while clock <= run:
        # Generate new random numbers for each T value
        for i in range(1, 5):
            x = random.random()
            x = round(x, 6)
            t[i] = int(1000 + x * 1000)

        # Print the current clock time and T values
        print(f"\n {clock:>5} {t[1]:>5} {t[2]:>5} {t[3]:>5} {t[4]:>5} {kont:>5}")

        # Find the smallest T value
        small = 999999
        for i in range(1, 5):
            if t[i] < small:
                small = t[i]

        # Update the clock time and increment the kont counter
        clock += small
        kont += 1

    # Calculate costs for both policies
    cost1 = count * (200 + 100) # Shut down cost 200 , cost of tube 100
    cost2 = kont * 2 * 200 + kont * 4 * 100

    # Print the calculated costs for both policies
    print(f"\nCost Present policy  = {cost1}\nCost proposed policy = {cost2}")

if __name__ == "__main__":
    main()
