import random
import scipy.stats as stats


# def generate_random_number():
#     return random.randint(1000, 9999)
# # Generate a sequence of 10,000 random four-digit numbers
# random_numbers = [generate_random_number() for _ in range(10000)]

observed_frequencies = {
    'Four different digits': 5120,
    'One pair in the digits': 4230,
    'Two pairs': 560,
    'Three digits of one kind': 75,
    'All four digits of one kind': 15
}

total_numbers = sum(observed_frequencies.values())


# if random number not given in question
# total_numbers = len(random_numbers)
# for num in random_numbers:
#     digits = [int(d) for d in str(num)]
#     digit_counts = [digits.count(d) for d in set(digits)]

#     if len(set(digits)) == 4:
#         observed_frequencies['Four different digits'] += 1
#     elif 2 in digit_counts:
#         observed_frequencies['One pair in the digits'] += 1
#     elif digit_counts.count(2) == 2:
#         observed_frequencies['Two pairs'] += 1
#     elif 3 in digit_counts:
#         observed_frequencies['Three digits of one kind'] += 1
#     elif all(count == 4 for count in digit_counts):
#         observed_frequencies['All four digits of one kind'] += 1

print("Observed frequencies:")
for combination, count in observed_frequencies.items():
    print(f"{combination}: {count} ({count / total_numbers * 100:.2f}%)")

expected_frequencies = {
    'Four different digits': total_numbers * 0.504,
    'One pair in the digits': total_numbers * 0.432,
    'Two pairs': total_numbers * 0.054,
    'Three digits of one kind': total_numbers * 0.009,
    'All four digits of one kind': total_numbers * 0.001
}

print("===")
print(expected_frequencies)
print("===")

chi_square = 0
for combination in observed_frequencies:
    observed = observed_frequencies[combination]
    expected = expected_frequencies[combination]
    chi_square += (observed - expected) ** 2 / expected

print("Chi-square statistic:", chi_square)
# Compare chi_square value with critical chi-square value at desired significance level


# Your code to calculate the chi-square statistic

# Degrees of freedom for the chi-square test
df = len(observed_frequencies) - 1

# Significance level (alpha)
alpha = 0.05

# Critical chi-square value
critical_chi_square = stats.chi2.ppf(1 - alpha, df)

if chi_square > critical_chi_square:
    print("Reject the null hypothesis. The random numbers are not independent.")
else:
    print("Not reject the null hypothesis. The random numbers are independent.")

