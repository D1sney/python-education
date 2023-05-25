


class Animal:
    
    color = '___'
    size = 'as'

    def __init__(self, color, size):
        self.color = color
        self.size = size
        print('1')
        

    def name(self):
        print('I`m animal')
        print('my color',self.color)
        print('my size',self.size)
        
    def voice(self):
        print('RRRRRRR')

    def voice2(self):
        print('BRRR')


class Car:

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def ride(self):
        print(self.speed)

    def name(self):
        # print('brand', self.__brand)
        print('color', self.color)




class Dog(Animal, Car):    

    def __init__(self, color, col, speed):
        print('2')
        self.speed = speed
        # Animal.__init__(self, 'blue', col)
        self.c = self.color
        self.amount = self.size*3
        

    def name(self):
         print(self.amount)
        #  self.ride()

    def voice(self):
        Car.__init__(self, 'purple', 140)
        print('WAF WAF')
        # self.voice2()
        Animal.voice(self)

    def ride(self):
        print(self.speed)
        






a = Animal('black', 'huge')
d = Dog('green', 150, 100)
c = Car('Yellow', 90)

listok = [a,d,c]
# d.voice()

d.name()

# for i in listok:
#     if isinstance(i, (Car, Dog)):
#         i.ride()
#     else:
#         print('это не тачка')



# if isinstance(d, (Car, test2.Bomba)):
#     print('of course')
# else:
#     print('also no')

# if issubclass(Dog, (test2.Bomba, Car, Animal)):
#     print('of course')
# else:
#     print('also no')