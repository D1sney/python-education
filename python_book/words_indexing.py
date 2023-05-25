file = open(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\transcript.txt', 'r', encoding='UTF-8')
text = file.read()
file.close()
words = text.split()
lines = text.split('\n')
newlines = []
for i in lines:
    a = i.split()
    newlines.append(a)
words_indexes = {}
words_indexes = words_indexes.fromkeys(set(words))   # при этом методе если указать по умолчанию например список, то все списки будут ссылаться на один и тот же объект списка и это приведет к неправильным результатам если не пропустить через цыкл и заново не присвоить список (все значения в словаре будут ссылаться на один и тот же список)

for i in words_indexes:
    words_indexes[i]=[]

for i in words_indexes:
    # print(i, words_indexes[i])
    for a in range(len(newlines)):
        # print(a, newlines[a])
        if i in newlines[a]:
            words_indexes[i].append(a+1)

for i in words_indexes:
    print(i, end=' ')
    for a in words_indexes[i]:
        print(a, end=' ')
    print()