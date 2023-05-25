import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, show

x_coords =[2,3,4,5,4]
y_coords = [1,3,1,5,2]

x_coords2 = [0,0,1,2,0]
y_coords2 = [-2,-3,1,0,1]

x_coords_stolb = [-4,-1,0,3,6]
y_coords_stolb = [-7,-5,2,4,-1]


# plt.plot(x_coords,y_coords)
# plt.show()

plot(x_coords,y_coords, 'v', color='k')

plt.bar(x_coords_stolb, y_coords_stolb, 1)

plt.title('Пример')
plt.xlabel('Это икс')
plt.ylabel('Это игрик')

plt.xlim(-5,10)
plt.ylim(-10, 15)
plot(x_coords2,y_coords2, marker='D', color='r')
plt.xticks([-15,2,2.3],
           ['Harry', 'Potter', 'Siuuu'])
plt.yticks([4,6],
           [4,'wow'])
plt.grid(True)

show()

bar_width = 0.4
colors = ['b', 'r', 'g', 'y']
plt.bar([0,1.5,1,4,5], [2,-1,3,4,5], bar_width, color=colors)



show()

labels = ('First', 'Second', "Third", 4)        # не имеет значения передавать в качестве аргумента список или кортеж
values = [20,60,80,40]
plt.pie(values, labels=labels, colors=colors)
plt.title('Circle-Кружок')

show()