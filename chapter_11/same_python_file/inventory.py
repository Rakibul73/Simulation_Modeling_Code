import random

# Initialize a counter for the number of simulations
m = 0

# Loop to perform simulations until m reaches 5
while m != 5:
    # Get user input for reorder point and reorder quantity
    reorder_point = int(input("\n Enter reorder point: "))
    reorder_quantity = int(input("\n Enter reorder quantity: "))
    
    # Initialize variables for inventory and costs
    units = 0
    equivalent_stock = 0
    day = 1
    due_day = 0
    demand = 0
    total_cost = 0
    current_stock = 115
    
    # Loop for each day in the simulation period (180 days)
    while day <= 180:
        # Check if an order is due on the current day
        if due_day == day:
            # Increase inventory and reset units ordered
            current_stock += reorder_quantity
            units = 0
        
        # Generate random demand for the day
        demand = random.randint(0, 99)
        
        # Calculate cost based on demand and inventory level
        if demand <= current_stock:
            current_stock -= demand
            total_cost += current_stock * 0.75
        else:
            total_cost += (demand - current_stock) * 18
            current_stock = 0
        
        # Calculate equivalent stock (inventory + ordered units)
        equivalent_stock = current_stock + units
        
        # Check if inventory is below reorder point
        if equivalent_stock <= reorder_point:
            # Place an order and incur ordering cost
            units = reorder_quantity
            total_cost += 75
            due_day = day + 3  # Set the due day for the ordered units
        
        # Move to the next day
        day += 1
    
    # Print simulation results for the current reorder point and reorder quantity
    print("\n Reorder point:", reorder_point)
    print(" Reorder Quantity:", reorder_quantity)
    print(" Total cost is:", total_cost)
    
    # Increment the simulation counter
    m += 1
