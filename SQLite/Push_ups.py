import sqlite3
import random
from datetime import datetime

BAFFS = ['Knuckles', 'Clap', 'ChairLeg', 'Narrow', 'Chill', 'Common', 'Common', 'Common', 'Common', 'Common']
COLUMNS = ['Day', 'Date', 'Time', 'CheckList', 'Count', 'Baff']

def main():
    while True:
        choice = show_menu()
        if choice == '1':
            add_user()
        elif choice == '2':
            delete_user()
        elif choice == '3':
            show_all_days()
        elif choice == '4':
            add_day()
        elif choice == '5':
            update_day()
        elif choice == '6':
            delete_day()
        elif choice == '7':
            how_much()
        elif choice == '8':
            print('\nProgram finishing')
            break
        else:
            print('Incorrect value')



def show_menu():
    return input('''\nСhoose an action from the list:\n
    1 - Add a user
    2 - Delete a user
    3 - Show all days
    4 - Add new day
    5 - Update a day
    6 - Delete a day
    7 - Show how much is left
    8 - Finish the program\n
Your choice - ''')



def add_user():
    choice = input('\nEnter a user name - ')    
    try:    
        conn = sqlite3.connect('Push_ups.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')

        # таблица со всеми пользователями
        cur.execute('''CREATE TABLE IF NOT EXISTS Users (UserName TEXT PRIMARY KEY NOT NULL)''')

        cur.execute('''INSERT INTO Users (UserName) VALUES (?)''', (choice,))
        
        # таблица с записями каждого дня
        cur.execute(f'''CREATE TABLE {choice+'_Days'} (DayID INTEGER PRIMARY KEY NOT NULL,
                    Date TEXT,
                    Time TEXT,
                    Push_upsID INTEGER NOT NULL,
                    Push_upsCount INTEGER,
                    Push_upsBaff TEXT,
                    FOREIGN KEY (Push_upsID) REFERENCES {choice+'_CheckList'} (Push_upsID))''') # чтобы использовать в названии таблиц и столбцов пробелы или например "-" необходимо заключить название в ковычки
        
        # таблица с количеством выполнения каждой ячейки
        cur.execute(f'''CREATE TABLE {choice+'_CheckList'} (Push_upsID INTEGER PRIMARY KEY NOT NULL,
                    CountDone INTEGER NOT NULL)''')
        
        for i in range(30):
            cur.execute(f'''INSERT INTO {choice+'_CheckList'} (CountDone)
                        VALUES (0)''') # лучше не использовать названия таблиц и столбцов из двух слов или не по стандарту SQL, тоесть используя различные конфликтующие символы, потому что в дальнейшем будет проблемно постоянно обращаться к таблице, например при использовании плейсхолдеров

        conn.commit()
        print(f'\nUser {choice} successfully added\n')

    except sqlite3.Error as err:
        if str(err) == 'UNIQUE constraint failed: Users.UserName':
            print('\nThis user name is already taken')
        else:
            print('\nError in SQL:', err)
    finally:
        if conn != None:
            conn.close()



def delete_user():
    try:
        conn = sqlite3.connect('Push_ups.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        
        cur.execute('''SELECT UserName FROM Users''')
        users = cur.fetchall()
        list_users = []

        # цикл показывает всех пользователей и запрашивает пользователя на удаление
        while True:
            print('\nSelect the user to be deleted from the list:\n')
            for user in users:
                list_users.append(user[0])
                print('\t' + user[0])
            del_user = input('\nYour choice - ')
            if del_user in list_users:
                break
            else:
                print('\nIncorrect value')
        
        # удаление пользователя
        cur.execute('''DELETE FROM Users WHERE UserName == ?''', (del_user,))
        cur.execute(f'''DROP TABLE {del_user+'_Days'}''')
        cur.execute(f'''DROP TABLE {del_user+'_CheckList'}''')

        conn.commit()
        print(f'\nUser {del_user} successfully deleted\n')

    except sqlite3.Error as err:
        print('\nError in SQL:', err)
    finally:
        if conn != None:
            conn.close()



def show_all_days():
    try:
        conn = sqlite3.connect('Push_ups.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')

        cur.execute('''SELECT UserName FROM Users''')
        users = cur.fetchall()

        # вывод всех дней по каждому пользователю
        for user in users:
            cur.execute(f'''SELECT * FROM {user[0]+'_Days'}''')
            days = cur.fetchall()
            print(f'\n{user[0]}')
            print(f'{"Day":^10}{"Date":^10}{"Time":^10}{"CheckList":^10}{"Count":^10}{"Baff":^10}')
            for day in days:
                print(f'{day[0]:^10}{day[1]:^10}{day[2]:^10}{day[3]:^10}{day[4]:^10}{day[5]:^10}')
            print()

    except sqlite3.Error as err:
        print('\nError in SQL:', err)
    finally:
        if conn != None:
            conn.close()



def add_day():
    try:
        conn = sqlite3.connect('Push_ups.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')

        cur.execute('''SELECT UserName FROM Users''')
        users = cur.fetchall()
        list_users = []

        # цикл показывает всех пользователей и запрашивает пользователя которому добавить новый день
        while True:
            print('\nSelect the user to add a new day from the list:\n')
            for user in users:
                list_users.append(user[0])
                print('\t' + user[0])
            select_user = input('\nYour choice - ')
            if select_user in list_users:
                break
            else:
                print('\nIncorrect value')
        
        # генерируются варианты для выбора
        v1 = []
        v1.append(random.choice(range(1,31)))
        v1.append(random.choice(BAFFS))

        v2 = []
        v2.append(random.choice(range(1,31)))
        v2.append(random.choice(BAFFS))

        v3 = []
        v3.append(random.choice(range(1,31)))
        v3.append(random.choice(BAFFS))
        
        count_variations = random.randint(1,3)
        
        # цикл показывает всех пользователей и запрашивает пользователя которому добавить новый день
        while True:
            
            # три вариации отжиманий на выбор
            if count_variations == 3:    
                print('\nСhoose a push-up variation of 1, 2 or 3 for today:\n')
                print(f'\t1 - {v1[1]} {v1[0]}')
                print(f'\t2 - {v2[1]} {v2[0]}')
                print(f'\t3 - {v3[1]} {v3[0]}')
                select_variation = input('\nYour choice - ')
                if select_variation in ['1','2','3']:
                    if select_variation == '1':
                        select_variation = v1
                    if select_variation == '2':
                        select_variation = v2
                    if select_variation == '3':
                        select_variation = v3        
                    break
                else:
                    print('\nIncorrect value')
            
            # две вариации отжиманий на выбор
            elif count_variations == 2:
                print('\nСhoose a push-up variation of 1 or 2 for today:\n')
                print(f'\t1 - {v1[1]} {v1[0]}')
                print(f'\t2 - {v2[1]} {v2[0]}')
                select_variation = input('\nYour choice - ')
                if select_variation in ['1','2']:
                    if select_variation == '1':
                        select_variation = v1
                    if select_variation == '2':
                        select_variation = v2        
                    break
                else:
                    print('\nIncorrect value')
        
            # одна вариация отжиманий на выбор
            elif count_variations == 1:
                print('\nYou have only one push-up variation for today, select "1" for choose it:\n')
                print(f'\t1 - {v1[1]} {v1[0]}')
                select_variation = input('\nYour choice - ')
                if select_variation == '1':
                    select_variation = v1
                    break
                else:
                    print('\nIncorrect value')

        # получение даты и времени
        current_date = str(datetime.now().date())
        current_time = str(datetime.now().time()).split(':')[0]+':'+str(datetime.now().time()).split(':')[1]
        
        # добавление нового дня в таблицу Days
        if select_variation[1] == 'Chill':
            cur.execute(f'''INSERT INTO {select_user+'_Days'} (Date, Time, Push_upsID, Push_upsCount, Push_upsBaff)
                        VALUES (?, ?, ?, ?, ?)''', (current_date, current_time, select_variation[0], 0, select_variation[1]))
        else:
            cur.execute(f'''INSERT INTO {select_user+'_Days'} (Date, Time, Push_upsID, Push_upsCount, Push_upsBaff)
                        VALUES (?, ?, ?, ?, ?)''', (current_date, current_time, select_variation[0], select_variation[0], select_variation[1]))

        # увеличение количества выполненых дней в таблице CheckList
        cur.execute(f'''SELECT CountDone FROM {select_user+'_CheckList'} WHERE Push_upsID == ?''', (select_variation[0],))
        count_done = cur.fetchone()[0]
        cur.execute(f'''UPDATE {select_user+'_CheckList'} SET CountDone = ? WHERE Push_upsID == ?''', (count_done+1, select_variation[0]))

        conn.commit()
        print(f'\nNew day {current_date} successfully added\n')

    except sqlite3.Error as err:
        print('\nError in SQL:', err)
    finally:
        if conn != None:
            conn.close()



def update_day():
    try:
        conn = sqlite3.connect('Push_ups.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')

        cur.execute('''SELECT UserName FROM Users''')
        users = cur.fetchall()
        list_users = []

        # цикл показывает всех пользователей и запрашивает имя пользователя
        while True:
            print('\nSelect the user:\n')
            for user in users:
                list_users.append(user[0])
                print('\t' + user[0])
            select_user = input('\nYour choice - ')
            if select_user in list_users:
                break
            else:
                print('\nIncorrect value')

        cur.execute(f'''SELECT DayID FROM {select_user+'_Days'}''')
        not_list_days = cur.fetchall()
        days = []
        for day in not_list_days:
            days.append(str(day[0]))

        # цикл запрашивает ID дня
        while True:
            print('\nSelect the day id:\n')
            print('\t', end='')        
            for day in days:
                print(day, end=' ')
            day_id = input('\n\nYour choice - ')
            if day_id in days:
                break
            else:
                print('\nIncorrect value')

        # цикл запрашивает название колонны
        while True:
            print('\nSelect the column:\n')
            for column in COLUMNS[1:]:
                print('\t' + column)
            column_name = input('\nYour choice - ')
            if column_name in COLUMNS[1:]:
                break
            else:
                print('\nIncorrect value')

        # цикл запрашивает новое значение для ячейки
        while True:
            if column_name in ['Date', 'Time', 'Baff']:
                new_value = input('Enter a text value - ')
                break
            elif column_name in ['CheckList', 'Count']:
                new_value = input('Enter an integer value - ')
                try:
                    new_value = int(new_value)
                    break
                except:
                    print('\nIncorrect value')
        
        # изменение данных по собранным параметрам
        if column_name == 'CheckList':
            cur.execute(f'''SELECT Push_upsID FROM {select_user+'_Days'} WHERE DayID == ?''', (day_id,))
            old_id = cur.fetchone()[0]
            cur.execute(f'''UPDATE {select_user+'_Days'} SET Push_upsID = ? WHERE DayID == ?''', (new_value, day_id))
            cur.execute(f'''UPDATE {select_user+'_CheckList'} SET CountDone = CountDone - 1 WHERE Push_upsID == ?''', (old_id,))
            cur.execute(f'''UPDATE {select_user+'_CheckList'} SET CountDone = CountDone + 1 WHERE Push_upsID == ?''', (new_value,))
        elif column_name == 'Date':
            cur.execute(f'''UPDATE {select_user+'_Days'} SET Date = ? WHERE DayID == ?''', (new_value, day_id))
        elif column_name == 'Time':
            cur.execute(f'''UPDATE {select_user+'_Days'} SET Time = ? WHERE DayID == ?''', (new_value, day_id))
        elif column_name == 'Date':
            cur.execute(f'''UPDATE {select_user+'_Days'} SET Date = ? WHERE DayID == ?''', (new_value, day_id))
        elif column_name == 'Count':
            cur.execute(f'''UPDATE {select_user+'_Days'} SET Push_upsCount = ? WHERE DayID == ?''', (new_value, day_id))
        elif column_name == 'Baff':
            cur.execute(f'''UPDATE {select_user+'_Days'} SET Push_upsBaff = ? WHERE DayID == ?''', (new_value, day_id))

        conn.commit()
        print(f'\nValue successfully updated\n')

    except sqlite3.Error as err:
        print('\nError in SQL:', err)
    finally:
        if conn != None:
            conn.close()



def delete_day():
    try:
        conn = sqlite3.connect('Push_ups.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')

        cur.execute('''SELECT UserName FROM Users''')
        users = cur.fetchall()
        list_users = []

        # цикл показывает всех пользователей и запрашивает имя пользователя
        while True:
            print('\nSelect the user:\n')
            for user in users:
                list_users.append(user[0])
                print('\t' + user[0])
            select_user = input('\nYour choice - ')
            if select_user in list_users:
                break
            else:
                print('\nIncorrect value')

        cur.execute(f'''SELECT DayID FROM {select_user+'_Days'}''')
        not_list_days = cur.fetchall()
        days = []
        for day in not_list_days:
            days.append(str(day[0]))

        # цикл запрашивает ID дня
        while True:
            print('\nSelect the day id:\n')
            print('\t', end='')        
            for day in days:
                print(day, end=' ')
            day_id = input('\n\nYour choice - ')
            if day_id in days:
                break
            else:
                print('\nIncorrect value')

        # изменение данных по собранным параметрам
        cur.execute(f'''SELECT Push_upsID FROM {select_user+'_Days'} WHERE DayID == ?''', (day_id,))
        push_ups_id = cur.fetchone()[0]
        cur.execute(f'''UPDATE {select_user+'_CheckList'} SET CountDone = CountDone - 1 WHERE Push_upsID == ?''', (push_ups_id,))
        cur.execute(f'''DELETE FROM {select_user+'_Days'} WHERE DayID == ?''', (day_id,))

        conn.commit()
        print(f'\nDay successfully deleted\n')

    except sqlite3.Error as err:
        print('\nError in SQL:', err)
    finally:
        if conn != None:
            conn.close()



def how_much():
    try:
        conn = sqlite3.connect('Push_ups.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')

        cur.execute('''SELECT UserName FROM Users''')
        users = cur.fetchall()

        # вывод всех оставшихся ячеек по каждому пользователю
        for user in users:
            cur.execute(f'''SELECT Push_upsID FROM {user[0]+'_CheckList'} WHERE CountDone == 0''')
            boxes = cur.fetchall()
            print(f'\n{user[0]}')
            for box in boxes[:-1]:
                print(box[0], end=', ')
            print(boxes[-1][0])

    except sqlite3.Error as err:
        print('\nError in SQL:', err)
    finally:
        if conn != None:
            conn.close()


if __name__ == '__main__':
    main()