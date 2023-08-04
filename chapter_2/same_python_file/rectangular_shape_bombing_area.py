import numpy as np
import matplotlib.pyplot as plt

x = 1000
y = 600

standard_deviation_x = x / 2
standard_deviation_y = y / 2

number_of_simulation = 1
number_of_strike_each_simulation = 20

for i in range(number_of_simulation):
    hit = 0
    miss  = 0
    point_x = []
    point_y = []
    for i in range(number_of_strike_each_simulation):
        normal_random_num = np.random.randn()
        current_x = standard_deviation_x*normal_random_num
        normal_random_num = np.random.randn()
        current_y = standard_deviation_y*normal_random_num
        point_x.append(current_x)
        point_y.append(current_y)
        
        if abs(current_x) <= standard_deviation_x and abs(current_y) <= standard_deviation_y :
            hit += 1
        else:
            miss += 1
    
    print("Number of hits =" ,hit)
    print("Number of miss =", miss)
    print("Number of Strikes on Target" , round(((hit/number_of_strike_each_simulation)*100) , 2) , "%")
    
    area_x = [-500, 500, 500, -500, -500]
    area_y = [-300, -300, 300, 300, -300]

    plt.plot(area_x, area_y, color="blue")
    plt.scatter(point_x, point_y, color="red")
    plt.axis('equal')
    plt.show()

