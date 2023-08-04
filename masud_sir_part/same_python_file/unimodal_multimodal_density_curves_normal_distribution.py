import numpy as np
import matplotlib.pyplot as plt

# Generate a random sample from a normal distribution

sample_size = 1000
mean = 100
standard_deviation = 20

random_sample = np.random.normal(mean, standard_deviation, sample_size)

# Plot the histogram of the blood pressure distribution

plt.hist(random_sample, bins=20, density=True, alpha=0.6, color='blue')
plt.xlabel('Blood Pressure')
plt.ylabel('Density')
plt.title('Histogram of Blood Pressure Distribution')
plt.show()

# Plot the unimodal density curves

x = np.linspace(min(random_sample), max(random_sample), 200)
unimodal_curve = (1 / (standard_deviation * np.sqrt(2 * np.pi))) * np.exp(-((x - mean) ** 2) / (2 * standard_deviation ** 2))

# Plot the multimodal density curves
mean2 = 80
standard_deviation2 = 20
multimodal_curve = (1 / (standard_deviation * np.sqrt(2 * np.pi))) * np.exp(-((x - mean) ** 2) / (2 * standard_deviation ** 2)) + (1 / (standard_deviation2 * np.sqrt(2 * np.pi))) * np.exp(-((x - mean2) ** 2) / (2 * standard_deviation2 ** 2))

plt.plot(x, unimodal_curve, label='Unimodal')
plt.plot(x, multimodal_curve, label='Multimodal')
plt.xlabel('Blood Pressure')
plt.ylabel('Density')
plt.title('Density Curves of Normal Distribution')
plt.legend()
plt.show()
