# classroom = {'CS101':'3004', 'CS102':'4501','CS103':'6755' , 'CS104':'1244', 'CS105':'1411'}
# teacher = {'CS101':'Хайнс', 'CS102':'Альварадо','CS103':'Рич' , 'NT110':'Берк', 'CM241':'Ли'}
# time = {'CS101':'8:00', 'CS102':'9:00','CS103':'10:00' , 'NT110':'11:00', 'CM241':'13:00'}

# a = input('Введите номер курса: ')

# if a in classroom:
#     print(classroom[a])
# if a in teacher:
#     print(teacher[a])
# if a in time:
#     print(time[a])


d = {'CS101':{'classroom':'3004', 'teacher':'Хайнс', 'time':'8:00'},
     'CS102':{'classroom':'4501', 'teacher':'Альварадо', 'time':'9:00'},
     'CS103':{'classroom':'6755', 'teacher':'Рич', 'time':'10:00'},
     'CS104':{'classroom':'1244'},
     'CS105':{'classroom':'1411'},
     'NT110':{'teacher':'Берк', 'time':'11:00'},
     'CM241':{'teacher':'Ли', 'time':'13:00'}}

a = input('Введите номер курса: ')

if a in d:
    if 'classroom' in d[a]:
        print(d[a]['classroom'])
    if 'teacher' in d[a]:
        print(d[a]['teacher'])
    if 'time' in d[a]:
        print(d[a]['time'])
