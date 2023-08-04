import numpy as np
import matplotlib.pyplot as plt

x = 0
y = 0
radius = 500

standard_deviation_x = 500
standard_deviation_y = 300

number_of_simulation = 1
number_of_strike_each_simulation = 40
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
        
        if np.sqrt(current_x**2 + current_y**2) <= radius:
            hit += 1
        else:
            miss += 1
    
    print("Number of hits =" ,hit)
    print("Number of miss =", miss)
    print("Number of Strikes on Target" , round(((hit/number_of_strike_each_simulation)*100) , 2) , "%")
    
    theta = np.linspace(0, 2*np.pi, 100)
    circle_x = radius*np.cos(theta)
    circle_y = radius*np.sin(theta)

    plt.plot(circle_x, circle_y, color="blue")
    plt.scatter(point_x, point_y, color="red")
    plt.axis('equal')
    plt.show()
