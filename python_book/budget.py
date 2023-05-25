import matplotlib.pyplot as plt
plt.title('Мои расходы')
values = [350,1700,500,4000,7200,250,2000,150,2500]
labels = ['Макдональдс','Зал','Лего','Пломба','Мышка','Печенья','Футболка','Чехол','Клавиатура']
colors = ['r','b','k','r','c','b','g','y','c']
plt.pie(values,labels=labels,colors=colors)
plt.show()