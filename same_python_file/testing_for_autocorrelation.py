import numpy as np

# Random numbers provided
random_numbers = [49, 95, 82, 19, 41, 31, 12, 53, 62, 40, 87, 83, 26, 1, 91, 55, 38, 75, 90, 35, 71, 57, 27, 85, 52, 8, 35, 57, 88, 38, 77, 86, 29, 18, 9, 96, 58, 22, 8, 93, 85, 45, 79, 68, 20, 11, 78, 93, 21, 13, 6, 32, 63, 79, 54, 67, 35, 18, 81, 40, 62, 13, 76, 74, 76, 45, 29, 36, 80, 78, 95, 25, 52]

# Create pairs from the random numbers
pairs = []
for i in range(0, len(random_numbers) - 1):
    pairs.append((random_numbers[i], random_numbers[i+1]))

print(pairs)

print(len(pairs))

class_counts = np.zeros(9)
for pair in pairs:
    if pair[0] <= 33 and pair[1] <= 33:
        class_counts[0] += 1
    elif pair[0] <= 67 and pair[1] <= 33:
        class_counts[1] += 1
    elif pair[0] <= 100 and pair[1] <= 33:
        class_counts[2] += 1
    elif pair[0] <= 33 and pair[1] <= 67:
        class_counts[3] += 1
    elif pair[0] <= 67 and pair[1] <= 67:
        class_counts[4] += 1
    elif pair[0] <= 100 and pair[1] <= 67:
        class_counts[5] += 1
    elif pair[0] <= 33 and pair[1] <= 100:
        class_counts[6] += 1
    elif pair[0] <= 67 and pair[1] <= 100:
        class_counts[7] += 1
    elif pair[0] <= 100 and pair[1] <= 100:
        class_counts[8] += 1

# Calculate the expectation of pairs in each class
expected_counts = np.full(9, len(pairs) / 9)


# Calculate the chi-squared statistic
chi2_stat = np.sum((class_counts - expected_counts) ** 2 / expected_counts)

# Calculate the degrees of freedom
df = len(class_counts) - 1

# Calculate the critical value for alpha = 0.05
from scipy.stats import chi2
alpha = 0.05
critical_value = chi2.ppf(1 - alpha, df)

# Print the test results
print("Class Counts:", class_counts)
print("Expected Counts:", expected_counts)
print("Chi-squared statistic:", chi2_stat)
print("Critical value for alpha 0.05:", critical_value)
