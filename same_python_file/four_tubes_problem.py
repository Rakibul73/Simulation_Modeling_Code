import random
clock_limit = 6000
clock = 0
tube_replaced = 0
how_many_time = 0

T1 = 1000 + (100* random.randint(0,9))
T2 = 1000 + (100* random.randint(0,9))
T3 = 1000 + (100* random.randint(0,9))
T4 = 1000 + (100* random.randint(0,9))

while clock_limit >= clock:
    how_many_time += 1
    fails_first = min( T1 , T2 , T3 , T4)
    clock += fails_first
    T1 -= fails_first
    T2 -= fails_first
    T3 -= fails_first
    T4 -= fails_first
    if T1 == 0:
        T1 = 1000 + (100* random.randint(0,9))
        tube_replaced += 1
    if T2 == 0:
        T2 = 1000 + (100* random.randint(0,9))
        tube_replaced += 1
    if T3 == 0:
        T3 = 1000 + (100* random.randint(0,9))
        tube_replaced += 1
    if T4 == 0:
        T4 = 1000 + (100* random.randint(0,9))
        tube_replaced += 1

# Equipment has to be shutdown for 1 hour for replacing a tube
# the cost of one tube is Rs. 100,
# shut down time costs Rs. 200 per hour


print("Total maintenance Cost = Rs.", (tube_replaced*100) + (how_many_time*200))
