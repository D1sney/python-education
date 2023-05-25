
def get_marks():
    flag = "yes"
    all_marks = []
    number = 1
    while flag == "yes":
        mark = input(f'Ведите оценку номер {number}: ')
        number +=1
        all_marks.append(mark)
        if input('Желаете продолжить? yes or no: ') != 'yes':
            flag = "no"
    return all_marks
 
def average_marks(values):
    average = 0
    laps = [] + values
    for mark in laps:
        try:
            print(values)
            print(mark)
            float(mark)
            print(type(mark))
            average += float(mark)
            values[values.index(mark)] = float(mark)

        except:
            values.remove(mark)

        # if type(mark) == str:
        #     values.remove[mark]
        # else:
        #     average += mark
    print(values)
    average -= min(values)
    values.remove(min(values))
    average /= len(values)
    return values, average


def main():
    lemon = 'yes'
    name = input('Введите имя ученика: ')
    while lemon == 'yes':
        spisok, average_mark = average_marks(get_marks())
        print(f'Имя ученика: {name}\nЕго оценки: {spisok}\nЕго средний балл: {average_mark}')
        lemon = input('Ввести еще одного ученика? yes or no ')
        if lemon == "yes":
            name=input('Введите имя ученика: ')



if __name__ == "__main__":
    main()
    
