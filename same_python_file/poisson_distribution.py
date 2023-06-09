import math
import matplotlib.pyplot as plt
import numpy as np

def poisson_pmf(x, lambd):
    return (math.exp(-lambd) * (lambd**x)) / math.factorial(x)

# Parameters
calls_per_hour_5 = 5  # Average rate of 5 calls per hour
calls_per_hour_10 = 10  # Average rate of 10 calls per hour
calls_per_hour_15 = 15  # Average rate of 15 calls per hour

max_calls = 10  # Maximum number of calls

# Calculate probabilities
x = np.arange(max_calls + 1)
pmf_5 = [poisson_pmf(i, calls_per_hour_5) for i in x]
pmf_10 = [poisson_pmf(i, calls_per_hour_10) for i in x]
pmf_15 = [poisson_pmf(i, calls_per_hour_15) for i in x]


# Calculate and print probabilities
print("Number of Calls (x)   |   Probability (P(x; λ=5))   |   Probability (P(x; λ=10))   |   Probability (P(x; λ=15))")
print("---------------------------------------------------------------------------------------------------------------")
for i in range(len(x)):
    print(f"{x[i]:<21} |   {pmf_5[i]:<30.4e}|   {pmf_10[i]:<30.4e}|   {pmf_15[i]:<.4e}")
print("---------------------------------------------------------------------------------------------------------------")

# Plotting the PMF graph
plt.bar(x, pmf_5, label='λ = 5')
plt.bar(x, pmf_10, label='λ = 10', alpha=0.5)
plt.bar(x, pmf_15, label='λ = 15', alpha=0.2)
plt.xlabel('Number of Calls')
plt.ylabel('Probability')
plt.title('Probability Mass Function (PMF)')
plt.xticks(x)
plt.legend()
plt.show()
