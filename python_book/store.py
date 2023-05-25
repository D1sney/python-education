class Item:
    def __init__(self, name):
        self.__name = name
        while self.__name not in ['носки', 'кроссовки', 'футболка']:
            self.__name = input('Введите название товара: ')
        if self.__name == 'носки':
            self.__price = 250
        if self.__name == 'кроссовки':
            self.__price = 2000
        if self.__name == 'футболка':
            self.__price = 500

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price
    
    def __str__(self):
        pass
        # return self.__name        # фушкция __str__ может возвращать только строковый тип значения 
    


class Store:
    def __init__(self):
        self.__store = {'носки':4, 'кроссовки':1, 'футболка':2}

    def set_store(self, name, action):
        if action == 'minus':
            if self.__store[name] > 0:
                self.__store[name] -= 1
            else:
                print('Товар закончиля на складе')
                return 'empty'
        if action == 'plus':
            self.__store[name] += 1

    def get_store(self):
        return self.__store
    
    def __str__(self):
        pass
        # return self.__name        # фушкция __str__ может возвращать только строковый тип значения 

store = Store()

class Client:
    def __init__(self):
        self.__bucket = []

    def adding(self, name):
        item = Item(name)
        if store.set_store(name, 'minus') != 'empty':
            self.__bucket.append(item)

    def deleting(self, name):
        for i in self.__bucket:
            if i.get_name() == name:
                self.__bucket.remove(i)
                store.set_store(name, 'plus')
                break
        
    def clear(self):
        for i in self.__bucket:
            store.set_store(i.get_name(),'plus')    
        self.__bucket = []

    def change(self, delname, addname):
        if addname in store.get_store():
            if store.get_store()[addname] > 0:
                for i in self.__bucket:
                    if i.get_name() == delname:
                        self.deleting(delname)
                        self.adding(addname)
                        break
            else:
                print('Товар который вы хотите добавить отсутствует на складе')
        else:
            print('Товара который вы хотите добавить нет в ассортименте')

    def show_items(self):
        for i in self.__bucket:
            print(i.get_name(), end=' ')
        print()

    def show_total(self):
        total = 0
        for i in self.__bucket:
            total += i.get_price()
        print(total)    



me = Client()
you = Client()
me.adding('носки')
me.adding('футболка')
me.adding('носки')
me.show_items()
me.show_total()
print(store.get_store())
me.deleting('носки')
me.show_items()
me.show_total()
print(store.get_store())
me.change('футболка', 'кроссовки')
me.show_items()
me.show_total()
print(store.get_store())
me.adding('кроссовки')
me.show_items()
me.show_total()
print(store.get_store())
you.adding('футболка')
you.show_items()
you.show_total()
print(store.get_store())