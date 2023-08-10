import random

# Seed for random number generation
SEED = 12345

def main():
    n = 6
    m = 5
    s = 4
    
    p = [0, 0.05, 0.4, 0.65, 0.80, 0.90, 0.97, 1.0]
    at = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    f = [0, 0.05, 0.3, 0.65, 0.85, 1, 0]
    t = [1, 2, 3, 4, 5]
    se = [0.0] * 10
    
    num_runs = int(input("Enter the value of num_runs: "))

    for j in range(2, s + 1):
        print("\nRun Length\tAverage Waiting time for S={}".format(j))
        for run in range(50, 501, 100):
            avg_waiting_time = 0.0
            for kk in range(1, num_runs + 1):
                random.seed(SEED)
                # Initialize the variables
                counter = 0
                nat = 0.0
                cwt = 0.0
                for i in range(1, j + 1):
                    se[i] = 0.0

                
                # Run the simulation for prescribed length of run
                for counter in range(1, run + 1):
                    # Generate the interarrival and service times for the new arrival
                    r_old = random.random()
                    r = round(r_old, 6)
                    # print(round(r, 6))
                    for i in range(n + 1):
                        if p[i] < r <= p[i + 1]:
                            iat = at[i]
                    r_old = random.random()
                    r = round(r_old, 6)
                    for i in range(m + 1):
                        if f[i] < r <= f[i + 1]:
                            st = t[i]
                    
                    nat += iat

                    # Determine the earliest service ending and the bearer and update the statistics
                    min_time = 99.9
                    wt = 0
                    for i in range(1, j + 1):
                        if se[i] <= min_time:
                            min_time = se[i]
                            k = i
                    if nat <= min_time:
                        se[k] = min_time + st
                        wt = min_time - nat
                    else:
                        se[k] = nat + st

                    cwt = cwt + wt

                avg_waiting_time += cwt / run

            print("{}\t\t{:8.2f}".format(run, avg_waiting_time / num_runs))

if __name__ == "__main__":
    main()
