import random

# Profit Analysis Problem
# fc = Fixed cost.
# sp = Selling price.
# Variable cost is between vc_lower_limit and vc_upper_limit.
# If the reaction of the opponent is strong, sales could be sale_lower_limit to sale_upper_limit_strong,
# and if the reaction is weak, the sales could be sale_lower_limit to sale_upper_limit_weak.
# csr = Chances of a strong reaction.

# Input the number of simulation runs
num_runs = int(input("Enter the number of simulation runs: "))

# Initialize counters for tracking losses and profits
loss_count = 0
profit_count = 0

# Given constants and parameters
fixed_cost = 60000  # Fixed cost
selling_price = 10  # Selling price
csr = 0.6           # Chances of strong reaction
vc_lower_limit = 4.5  # Variable cost lower limit
vc_upper_limit = 5.5  # Variable cost upper limit
sale_lower_limit = 10000  # Lower limit of sales
sale_upper_limit_strong = 12000  # Upper limit of sales for strong reaction
sale_lower_limit_weak = 13000   # Lower limit of sales for weak reaction
sale_upper_limit_weak = 15000   # Upper limit of sales for weak reaction

# Loop for performing the simulation for 'num_runs' runs
for run in range(1, num_runs + 1):
    # Generate a random number between 0 and 1 with two decimal places for variable cost adjustment
    variable_cost_adjustment = round(random.uniform(0, 1), 2)
    # Calculate the adjusted variable cost
    variable_cost = vc_lower_limit + variable_cost_adjustment * (vc_upper_limit - vc_lower_limit)
    
    # Generate another random number between 0 and 1 with two decimal places to determine the opponent's reaction
    reaction_strength = round(random.uniform(0, 1), 2)
    # Determine the demand based on opponent's reaction
    if reaction_strength <= csr:
        demand = sale_lower_limit + reaction_strength * (sale_upper_limit_strong - sale_lower_limit)
    else:
        demand = sale_lower_limit_weak + reaction_strength * (sale_upper_limit_weak - sale_lower_limit_weak)
    
    # Calculate the profit for the current run
    profit = demand * (selling_price - variable_cost) - fixed_cost

    # Check if the profit is less than -5000 (indicating a loss)
    if profit < -5000:
        loss_count += 1
    
    # Check if the profit is greater than 5000 (indicating a profit)
    if profit > 5000:
        profit_count += 1

# Print the simulation results
print("\nNumber of simulation runs =", num_runs)
print("Probability of LOSS being greater than 5000 =", loss_count * 100 / num_runs)
print("Probability of PROFIT being greater than 5000 =", profit_count * 100 / num_runs)
