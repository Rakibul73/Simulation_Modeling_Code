import random
import scipy.stats as stats


# def generate_random_number():
#     return random.randint(100, 999)

# # Generate a sequence of 10,000 random five-digit numbers
# random_numbers = [generate_random_number() for _ in range(10000)]


observed_frequencies = {
    'All three of different kind': 680,
    'One pair': 289,
    'All three of same kind': 31
}


total_numbers = sum(observed_frequencies.values())

# if random number not given in question
# total_numbers = len(random_numbers)
# for num in random_numbers:
#     digits = [int(d) for d in str(num)]
#     digit_counts = [digits.count(d) for d in set(digits)]

#     if len(set(digits)) == 3:
#         observed_frequencies['All three of different kind'] += 1
#     elif 2 in digit_counts:
#         observed_frequencies['One pair'] += 1
#     elif all(count == 3 for count in digit_counts):
#         observed_frequencies['All three of same kind'] += 1


print("Observed frequencies:")
for combination, count in observed_frequencies.items():
    print(f"{combination}: {count} ({count / total_numbers * 100:.2f}%)")

expected_frequencies = {
    'All three of different kind': total_numbers * 0.72,
    'One pair': total_numbers * 0.27,
    'All three of same kind': total_numbers * 0.01
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


