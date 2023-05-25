import matplotlib.pyplot as plt
plt.title('График Pineapple')
plt.xlabel('Дата')
plt.ylabel('Цена')
x_coords = [1,2,3,4,5,6,7,8]
y_coords = [10000,12000,15000,13000,9000,14000,17000,15500]
plt.plot(x_coords,y_coords,marker='*',color='r')
plt.xticks(x_coords,
           [1,2,3,4,'Min',6,'Max',8])
plt.yticks(y_coords,
           ['10000$','12000$','15000$','13000$','9000$','14000$','17000$','16000$'])
plt.grid(True)

plt.show()