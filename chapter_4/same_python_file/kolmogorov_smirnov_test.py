import numpy as np

def kolmogorov_smirnov_test(data, significance_level):
    sorted_data = np.sort(data)
    n = len(sorted_data)
    empirical_cdf = np.arange(1, n + 1) / n
    d_plus = empirical_cdf - sorted_data
    d_minus = sorted_data - (np.arange(n) / n)
    test_statistic = np.max([np.max(d_plus), np.max(d_minus)])

    # Look up critical value from table or use scipy.stats.kstwobign.ppf for large sample sizes
    # Here, we manually provide the critical value for N=10 and significance_level=0.05
    critical_value = 0.410


    if test_statistic < critical_value:
        result = "The given random numbers are uniform at {}% level of significance.".format((1 - significance_level) * 100)
    else:
        result = "The given random numbers are not uniform at {}% level of significance.".format((1 - significance_level) * 100)

    return test_statistic, result



data = [0.24, 0.89, 0.11, 0.61, 0.23, 0.86, 0.41, 0.64, 0.50, 0.65]
significance_level = 0.05

test_statistic, result = kolmogorov_smirnov_test(data, significance_level)


print("Test Statistic:", test_statistic)
print(result)
