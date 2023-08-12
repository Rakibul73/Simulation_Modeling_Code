# simulate an inventory system with the objective to determine the
# re-order combination (P,Q) which yields the highest service level 
# for a given value of average stock.

import random
def main():
    # Initialize variables
    current_day = 1       # Counter for the current day
    current_stock = 10    # Current stock level
    cumulative_stock = 0  # Cumulative stock over days
    pending_order = 0     # Quantity of items pending in an order
    order_arrival_days = 0  # Days until the arrival of an order
    daily_demand = 0      # Demand for the current day
    cumulative_demand = 0 # Cumulative demand over days
    shortage_quantity = 0 # Quantity of shortages
    cumulative_shortage = 0 # Cumulative shortages over days
    reorder_point = 10    # Reorder point
    reorder_quantity = 15 # Reorder quantity
    lead_time = 3         # Lead time
    
    # Input: Length of simulation run (in days)
    simulation_days = int(input("\n Length of simulation run (tdays) = "))
    
    # Print initial parameter values
    print("\n Initial stock =", current_stock)
    print(" Lead time =", lead_time)
    print(" Reorder point =", reorder_point)
    print(" Reorder quantity =", reorder_quantity)
    
    # Simulation loop
    while current_day <= simulation_days:
        # Update stock based on daily demand
        current_stock = current_stock - daily_demand
        if current_stock <= 0:
            current_stock = 0
        
        # Handle the arrival of a pending order
        if order_arrival_days == 0:
            current_stock = current_stock + pending_order
            pending_order = 0
        
        # Update cumulative stock
        cumulative_stock = cumulative_stock + current_stock
        
        # Place a new order if stock is below the reorder point
        if pending_order == 0:
            if current_stock <= reorder_point:
                pending_order = reorder_quantity
                order_arrival_days = lead_time
        
        # Generate random daily demand
        random_value = random.random()
        if random_value <= 0.20:
            daily_demand = 3
        elif 0.20 < random_value <= 0.50:
            daily_demand = 4
        elif 0.50 < random_value <= 0.85:
            daily_demand = 5
        else:
            daily_demand = 6
        
        # Update cumulative demand
        cumulative_demand += daily_demand
        
        # Calculate shortage and update cumulative shortages
        if daily_demand > current_stock:
            shortage_quantity = daily_demand - current_stock
        else:
            shortage_quantity = 0
        cumulative_shortage += shortage_quantity
        
        # Decrement days until order arrival
        if order_arrival_days > 0:
            order_arrival_days = order_arrival_days - 1
        
        # Move to the next day
        current_day += 1
    
    # Calculate and print results
    service_level = (cumulative_demand - cumulative_shortage) * 100.0 / cumulative_demand
    average_stock = cumulative_stock / simulation_days
    print("\n Average stock = {:.2f} units, service level = {:.2f} %".format(average_stock, service_level))

if __name__ == "__main__":
    main()
