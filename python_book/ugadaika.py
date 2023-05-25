import random
def ugadaika(r):    
    x=random.randint(1,r)
    i =int(input('угадайте число '))
    p=1
    if i==x:
        print('С первой попытки!!!')
    while i != x:
        p+=1
        if i<x:
            print('возьмите число побольше')
        if i>x:
            print('возьмите число поменьше')
        i =int(input('попробуйте снова '))
    if p>1:
        print(f'Вы угадали!!! вам потребовалось {p} попыток.')

if __name__ == '__main__':
    while True:
        ugadaika(100)
