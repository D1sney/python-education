name_file = input('Введите какой файл открыть? ')
try:
    file = open(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\\'+ name_file +'.txt', 'r', encoding='utf8')

    amount = 0
    count = 0
    line = file.readline()
    try:
        while line != '':
            amount += float(line)
            count +=1
            line = file.readline()

    except ValueError:
        print('В файле есть буквы')
    finally:
        try:
            print(f'Среднефрифметическое всех чисел равно: {amount/count:,.2f}')
        except ZeroDivisionError:
            print('Первая строка и сразу буква')


    file.close()
except IOError:
    print('file don\'t search')