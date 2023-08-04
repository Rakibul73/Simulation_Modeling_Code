import numpy as np
import random

# Generate 100 random numbers (example)
random_numbers = []
i = 0
while i < 100:
    k = random.randint( 0 , 99)
    random_numbers.append(k)
    i += 1

print("Random num = ", random_numbers)

# Define the expected probabilities for each category (uniform distribution)
expected_probs = np.full(10, 10)
print("expected num in each category = ",expected_probs)


# Divide the random numbers into 10 categories
observed_counts, _ = np.histogram(random_numbers, bins=10)
print("frequency = " , observed_counts)

# Calculate the chi-squared statistic
chi2_stat = np.sum(abs(observed_counts - expected_probs) ** 2 / (expected_probs))

# Calculate the degrees of freedom (number of categories - 1)
from scipy.stats import chi2
df = 10 - 1  
# Calculate the critical value for alpha = 0.05
alpha = 0.05
critical_value = chi2.ppf(1 - alpha, df)

# Print the test results
print("Chi-squared statistic:", chi2_stat)
print("Critical value for alpha 0.05:", critical_value)
