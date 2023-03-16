import random
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
x_point = []
y_point = []

coords = [(1, 1), (10, 95), (40, 70), (50, 50),(30,20)]
map = Polygon(coords)

print("\n wait , program is running.........")

for i in coords:
    a = i[0]
    b = i[1]
    x_point.append(a)
    y_point.append(b)
x_point.append(x_point[0])
y_point.append(y_point[0])
plt.plot(x_point,y_point,color="red")

n=0
m=0
for i in range(2000):
    x = random.randint(0,50)
    y = random.randint(0,100)
    point = Point(x,y)
    n+=1
    if(map.contains(point)):
        m+=1
        plt.scatter(x,y ,color="blue")
        continue

    plt.scatter(x,y ,color="yellow")


plt.show()
print("Actual Area : ",map.area)
print("Predicted Area : ",(m/n)*(100*50))