import random

# Define the range of the dimensions
a_min = 1.95
a_max = 2.05
b_min = 1.95
b_max = 2.05
c_min = 29.5
c_max = 30.5
d_min = 34.0
d_max = 35.0

# Define the number of iterations
n = 1000

# Initialize the counters
not_assemble_count = 0
assemble_count = 0

# Generate the assemblies
for i in range(n):
    # Generate the dimensions
    a = a_min + round(random.random() , 2)
    b = b_min + round(random.random() , 2)
    c = c_min + round(random.random() , 2)
    d = d_min + round(random.random() , 2)



    # Check if the parts will assemble
    x = d - (a + b + c)
    if x >= 0:
        assemble_count += 1
    else:
        not_assemble_count += 1

# Calculate the probabilities
not_assemble_prob = not_assemble_count / n
assemble_prob = assemble_count / n


print(f"Number of assemblies: {n}")
print(f"Number of assemblies that do not assemble: {not_assemble_count}")
print(f"Number of assemblies that assemble: {assemble_count}")
print(f"Probability that the selected parts will not assemble: {not_assemble_prob} or {not_assemble_prob*100} %")
print(f"Probability that the selected parts will assemble: {assemble_prob} or {assemble_prob*100} %")
