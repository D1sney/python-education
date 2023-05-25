right_answers = ['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','C','B','B','D','A']
file = open(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\exam.txt', 'r')
answers = file.readlines()
# print(answers)
for i in range(len(answers)):
    answers[i] = answers[i].rstrip('\n')
# print(answers)
wrong_answers = []
count_wrong = 0
for i in range(len(right_answers)):
    try:
        if answers[i] != right_answers[i]:
            count_wrong += 1
            wrong_answers.append(i+1)
    except:
        count_wrong += 1
        wrong_answers.append(i+1)
if count_wrong>5:
    print('Вы провалили экзамен!!!')
else:
    print('Поздравляю вы прошли экзамен!!!')
print(f'Вы ответили неправильно на {count_wrong} вопросов\nВот список вопросов на которые вы ответили неверно:')
for i in wrong_answers:
    print(i, end=' ')