import numpy as np
import matplotlib.pyplot as plt

# Generate random samples from normal distributions
sample_size = 200
mean_diastolic = 80
std_diastolic = 20
mean_sample = 100
std_sample = 20

random_sample_diastolic = np.random.normal(mean_diastolic, std_diastolic, sample_size)
random_sample_sample = np.random.normal(mean_sample, std_sample, sample_size)

# Plot histogram of the diastolic blood pressure distribution
plt.hist(random_sample_diastolic, bins=20, density=True, alpha=0.6, color='blue', label='Diastolic Blood Pressure')
plt.xlabel('Blood Pressure')
plt.ylabel('Density')
plt.title('Histogram of Diastolic Blood Pressure Distribution')
plt.legend()
plt.show()

# Plot histogram of the sample distribution
plt.hist(random_sample_sample, bins=20, density=True, alpha=0.6, color='orange', label='Sample')
plt.xlabel('Blood Pressure')
plt.ylabel('Density')
plt.title('Histogram of Sample Blood Pressure Distribution')
plt.legend()
plt.show()

# Plot unimodal density curves
x = np.linspace(min(random_sample_diastolic), max(random_sample_sample), 200)
unimodal_curve_diastolic = (1 / (std_diastolic * np.sqrt(2 * np.pi))) * np.exp(-((x - mean_diastolic) ** 2) / (2 * std_diastolic ** 2))
unimodal_curve_sample = (1 / (std_sample * np.sqrt(2 * np.pi))) * np.exp(-((x - mean_sample) ** 2) / (2 * std_sample ** 2))

# Plot the multimodal density curve
mean2 = 80
std2 = 20
multimodal_curve = (1 / (std_diastolic * np.sqrt(2 * np.pi))) * np.exp(-((x - mean_diastolic) ** 2) / (2 * std_diastolic ** 2)) + (1 / (std2 * np.sqrt(2 * np.pi))) * np.exp(-((x - mean2) ** 2) / (2 * std2 ** 2))

plt.plot(x, unimodal_curve_diastolic, label='Diastolic Unimodal')
plt.plot(x, unimodal_curve_sample, label='Sample Unimodal')
plt.plot(x, multimodal_curve, label='Multimodal')
plt.xlabel('Blood Pressure')
plt.ylabel('Density')
plt.title('Density Curves of Blood Pressure Distributions')
plt.legend()
plt.show()
