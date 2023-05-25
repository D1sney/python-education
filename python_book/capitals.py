import random
import pickle


def main():
    try:
        file = open(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\capitals.dat', 'rb')
        towns = pickle.load(file)
    except:
        towns = dict()
    finally:
        file.close()
    print(towns)

    choice = input('1 - добавить новую столицу\n2 - начать играть\nВыберите действие: ')
    if choice =='1':
        addition(towns)
    elif choice == '2':
        play(towns)
    else:
        print('нет такого варианта')


def addition(capitals):    
    sign = True
    while sign:
        country = input('Введите название страны: ')
        capital = input('Введите название столицы: ')
        capitals[country]=capital

        if input('Желаете продолжить? (да/нет): ').upper() == 'ДА':
            pass
        else:
            sign = False
    file = open(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\capitals.dat', 'wb')
    pickle.dump(capitals, file)
    file.close()


def play(capitals):
    keys = capitals.keys()
    count = 0
    sign = True
    while sign:
        key = random.choice(list(keys))
        answer = input(f'Столица {key}: ')
        if answer.lower().strip() == capitals[key]:
            count += 1
            print('Правильный ответ!!!')
        else:
            sign = False
            print('Неправильный ответ(((')
    print(f'Ты ответил правильно на {count} вопроса')



if __name__ == '__main__':
    main()