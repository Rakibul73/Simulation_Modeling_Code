import random

m = 0
while m != 5:
    p = int(input("\n Enter reorder point: "))
    q = int(input("\n Enter reorder quantity: "))
    units = 0
    eqstock = 0
    start = 1
    due = 0
    demand = 0
    cost = 0
    stock = 115
    
    while start <= 180:
        if due == start:
            stock += q
            units = 0
        
        demand = random.randint(0, 99)
        
        if demand <= stock:
            stock -= demand
            cost += stock * 0.75
        else:
            cost += (demand - stock) * 18
            stock = 0
        
        eqstock = stock + units
        if eqstock <= p:
            units = q
            cost += 75
            due = start + 3
        
        start += 1
    
    print("\n Reorder point:", p)
    print(" Reorder Quantity:", q)
    print(" Total cost is:", cost)
    
    m += 1
