# date = '17/01/1989'
# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# print(date.split('/')[0], months[int(date.split('/')[1])-1], date.split('/')[2], 'year')


# number = '7425'
# index = 0
# total = 0
# while index<len(number):
#     total += int(number[index])
#     index += 1
# print(total)


# morza = ['.--', '-.--', ',..,', '---', ',,--']
# translate = ['1', '2', '3', '4', '5']
# text = '-.-- ,,-- --- --- ,.., .-- ,,-- -.--'
# a = text.split()
# print(a)
# b = ''
# for i in a:
#     b += translate[morza.index(i)]
# print(b)


stroka = 'who is there? i love you! hello! i can do it. sonic and shadow are the best friends.'
index = 0
first = 1
new_stroka = ''
signs = ['.', '?', '!']
for i in stroka:
    if first == 1:
        new_stroka += i.upper()
        first = 0
    elif i in signs:
        index += 1
        new_stroka += i
    elif index == 2:
        new_stroka += i.upper()
        index = 0
    else:
        new_stroka += i
        if index == 1:
            index += 1
print(new_stroka)