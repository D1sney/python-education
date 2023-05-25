import time
import os
import my_time

CHOOSING_TEXT = '''
Выберите действие из предложанных:
1 - Добавить запись о поставка кофе
2 - Количество сорта кофе на складе
3 - Удалить все записи о данном сорте кофе
4 - Удалить конкретную запись
'''

def dobavlenie():
    file = open(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\kofe.txt', 'a', encoding='utf8')
    name = input('Введите сорт кофе: ')
    amount = input('Введите количество кофе: ')
    file.write(name + '\n' + amount + '\n' + my_time.my_time() + '\n')
    print('Запись была добавлена\n')
    file.close()



def finder():
    search = input('Введите количество какого сорта кофе вы хотите узнать? ')
    file = open(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\kofe.txt', 'r', encoding='utf8')
    name = file.readline()
    found = False
    allcofe=0
    while name != '':
        amount = float(file.readline())
        ttime = file.readline()
        name=name.rstrip('\n')
        if name == search:
            allcofe+=amount
            found = True
            rtime =ttime
        name=file.readline()
    if found == False:
        print('Нет такого сорта кофе\n')
    else:
        print(f'Сорт: {search}\nВ количестве: {allcofe}\nПоследняя запись: {rtime}')



def udalenie(x):
    file=open(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\kofe.txt', 'r', encoding='utf8')
    newfile=open(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\vremennii_fail.txt', 'w', encoding='utf8')
    found = False
    if x == 1:
        search_name = input('Какой сорт кофе вы хотите удалить? ')
    elif x == 2:
        search_name = input('Какой сорт кофе был в записи? ')
        search_amount = input('Какое количество кофе было добавленно в данной записи? ')
        search_ttime = input('В какое время была сделана данная запись? ')
    name = file.readline()
    while name != '':
        name = name.rstrip('\n')
        amount = file.readline()
        ttime = file.readline()
        amount =amount.rstrip('\n')
        ttime =ttime.rstrip('\n')
        if x ==1 and name != search_name:
            newfile.write(name +'\n' + amount +'\n' + ttime + '\n')
        elif x ==1 and name == search_name: 
            found = True
        if x == 2 and (name != search_name or amount != search_amount or ttime != search_ttime):
            newfile.write(name +'\n' + amount +'\n' + ttime + '\n')
        elif x == 2 and (name == search_name and amount == search_amount and ttime == search_ttime):
            found = True
        name = file.readline()
    file.close()
    newfile.close()
    sure = 0
    if x == 1 and found == False:
        print('Такого сорта кофе не найдено\n')
    elif x==1:
        sure = input(f'Ты уверен что  что хочешь удалить сорт: {search_name}?\n"yes" or "no"\n')
    if x == 2 and found == False:
        print('Такой записи не было найдено\n')
    elif x==2:
        sure = input(f'Ты уверен что хочешь удалить данную запись?\n{search_name}\n{search_amount}\n{search_ttime}\n"yes" or "no"\n')
    if sure == 'yes':
        os.remove(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\kofe.txt')
        os.rename(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\vremennii_fail.txt', r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\kofe.txt')
    if sure != 'yes':
        os.remove(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\vremennii_fail.txt')
    if x==1 and found == True and sure == 'yes':
        print('Сорт кофе был удален\n')  
    elif x==1 and found == True and sure != 'yes':
        print('Отмена удаления сорта\n')
    if x==2 and found == True and sure == 'yes':
        print('Запись была удалена\n')  
    elif x==2 and found == True and sure != 'yes':
        print('Отмена удаления записи\n')
        


if __name__ == '__main__':
    x = input(CHOOSING_TEXT)
    if x == '1':
        dobavlenie()
    elif x == '2':
        finder()
    elif x == '3':
        udalenie(1)
    elif x == '4':
        udalenie(2)
    else:
        pass