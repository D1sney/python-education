import math
metres=float(input('Введите количество квадратных метров '))
rublit=float(input('Введите стоимость за литр краски '))
def mal(metres,rublit):
    lit=math.ceil(metres*0.5)
    kraska_price=math.ceil(lit*rublit)
    work_price=2000*math.ceil(metres/10)
    all_price=work_price + kraska_price
    hours,minutes=time(metres*0.8)
    print(f'* количество требуемых емкостей краски: {lit}\n\
* количество затраченных часов: {hours} часов, {minutes} минут\n\
* стоимость краски: {kraska_price:,}\n\
* стоимость работы: {work_price:,}\n\
* общая стоимость работ: {all_price:,}')

def time(x):
    if x//1 != x/1:
        i=x-x//1 
        minutes=round(60*i)
        hours=round(x//1)
    else:
        hours=round(x//1)
        minutes=0
    return hours, minutes

mal(metres,rublit)

