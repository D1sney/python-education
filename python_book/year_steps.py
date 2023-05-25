# import random_steps
# file = open(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\steps.txt', 'w', encoding='utf8')
# for i in range(365):
#     file.write(f'{random_steps.steps()}\n')
# file.close()

def calculate(mounth, days):
    amount = 0
    error = 0
    for i in range(days):
        x = file.readline()
        if error == 0:
            if x.rstrip('\n') =='':
                print('Файл закончился')
                error = 1
                break
            try:
                x = float(x)
            except ValueError:
                print('В Файле буква')
                error = 1
                continue
            amount+=x
    if error == 0:
        print(f'В {mounth} среднее количество шагов: {amount/days:,.0f}')

if __name__ == '__main__':
    file = open(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\steps.txt', 'r', encoding='utf8')
    calculate('January', 31)
    calculate('February', 28)
    calculate('March', 31)
    calculate('April', 30)
    calculate('May', 31)
    calculate('June', 30)
    calculate('Jule', 31)
    calculate('August', 31)
    calculate('September', 30)
    calculate('October', 31)
    calculate('November', 30)
    calculate('December', 31)
    file.close()