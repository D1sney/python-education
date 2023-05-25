import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

# поддержка внешних ключей
cur.execute('PRAGMA foreign_keys=ON')

# создание бд
cur.execute('''CREATE TABLE IF NOT EXISTS Inventory (ItemID INTEGER PRIMARY KEY NOT NULL,
            ItemName TEXT,
            Price REAL NOT NULL,
            PlaceID INTEGER,
            FOREIGN KEY (PlaceID) REFERENCES Places (PlaceID))''') # в этой строчке создается внешний ключ

cur.execute('''CREATE TABLE IF NOT EXISTS Places (PlaceID INTEGER PRIMARY KEY NOT NULL,
            City TEXT)''')

# создание таблицы с состовными ключами
cur.execute('''CREATE TABLE IF NOT EXISTS Classrooms (RoomNumber INTEGER NOT NULL,
            Building TEXT NOT NULL,
            Seats INTEGER,
            PRIMARY KEY(RoomNumber, Building))''') # состовной PRIMARY KEY не может самостоятельно увеличиваться на один в каждой новой строке, также если не указывать в создании таблицы NOT NULL то он может содержать значение NULL

name = 'Ветровка'
cost = 300

# занесение строк в бд
cur.execute('''INSERT INTO Inventory (ItemName, Price)
            VALUES (?, 500),
            ('Шапка', 300), 
            ('Куртка', ?)''', # нельзя игнорировать в новой строке столбец в котором задано NOT NULL, за исключением INTEGER PRIMARY KEY
            (None, cost-150)) # если сюда передавать только одну переменную, то после нее надо поставить запятую, потому что аргуемнт принимает кортеж

cur.execute('''INSERT INTO Places (City) 
            VALUES (?), ("London")''', 
            ('Moscow',)) 

cur.execute('''INSERT INTO Inventory (ItemName, Price, PlaceID)
            VALUES ("Футболка", 550, 1)''')

# чтение бд всех строк
cur.execute('''SELECT ItemName, Price FROM Inventory''') # чтобы выбрать сразу все столбцы можно использовать *
all = cur.fetchall()
for i in all:
    print(i[0], i[1])
print(cur.fetchall()) # при повторном вызове этого метода или если вы не вызвли SELECT, он вернет пустой список

# чтение бд по одной строке
cur.execute('''SELECT ItemName, Price FROM Inventory''')
i = cur.fetchone()
while i != None:
    print(i[0], i[1])
    i = cur.fetchone() # если вызвать fetchone() после fetchall() то он вернет None, а если наоборот то fetchall() вернят список оставшихся строк в таблице (строки которые не обрабатывали предыдущие инструкции fetchone())
print(cur.fetchone()) # когда строки закончатся или если вы не вызвали SELECT, он вернет пустой список

# удаление таблицы
cur.execute('''DROP TABLE IF EXISTS Inventory''')

# чтение бд с операторами WHERE, AND, NOT, OR, LIKE, ORDER BY
# ORDER BY сортирует результат возвращаемых строк ПО ОПРЕДЕЛЕННОМУ СТОЛБЦУ от меньшего значения к большему, если вы хотите отсортировать значения от большего к меньшего, необходимо дополнительно добавть в конце инструкцию - DESC, этот параметр сортирует строку именно по количеству букв
cur.execute('''SELECT * FROM Inventory WHERE Price >= ? AND NOT Lower(ItemName) == ?
            ORDER BY Price DESC''', (cost, 'mug')) # оператор WHERE фильтрует возвращаемые строки по различным условиям, функция Lower() в SQL работает только с английскими буквами
cur.execute('''SELECT * FROM Inventory WHERE ItemName LIKE "%ка%" 
            ORDER BY ItemName''') # с каких сторон ставятся % от подстроки, с тех сторон может быть продолжение строки и условие будет выполняться
cur.execute('''SELECT * FROM Inventory WHERE ItemName IS NULL''') # только таким способом стобец проверяется на NULL, если проверя через оператор == NULL, то он не найдет эти строки
print(cur.fetchall())

# чтение бд - агрегатные функции
cur.execute('''SELECT AVG(Price) FROM Inventory''') # AVG() возвращает среднее значение всех чисел в выбранном столбце, она игнорирует строковые значения в стобце
cur.execute('''SELECT SUM(Price) FROM Inventory''') # SUM() возвращает сумму всех чисел в выбранном столбце, она игнорирует строковые значения в стобце
cur.execute('''SELECT MIN(Price) FROM Inventory WHERE ItemName LIKE "%g%"''') # MIN() возвращает наименьшее значение всех чисел в выбранном столбце, она игнорирует строковые значения в стобце
cur.execute('''SELECT MAX(Price) FROM Inventory''') # MAX() возвращает наибольшее значение всех чисел в выбранном столбце, она игнорирует строковые значения в стобце
cur.execute('''SELECT COUNT(Price) FROM Inventory''') # COUNT() возвращает количество всех строк в выбранном столбце не считая строк со значением NULL
print(cur.fetchone()[0])

# чтение нескольких столбцов из разных таблиц
cur.execute('''SELECT Inventory.ItemName, Inventory.Price, Places.City FROM Inventory, Places WHERE Inventory.PlaceID == Places.PlaceID''') # при соединении данных из нескольких таблиц следует указать критерии поиска связывающие соответствущие столбцы, чтобы не получился большой объем не связанных между собой данных - подходящие критерии указаны после WHERE в данном примере
print(cur.fetchall())

# обновление строк в бд
cur.execute('''UPDATE Inventory SET ItemName = "Худи", Price = ? WHERE ItemID == ? OR ItemID == ?''', (777, 12, 15)) # после SET, можно передать несколько столбцов для изменения
cur.execute('''UPDATE Inventory SET ItemName = "Худи", Price = ? WHERE ItemID == ? OR ItemID == ?''', (777, 16, 16)) # после SET, можно передать несколько столбцов для изменения
print(cur.rowcount) # атрибут rowcount показывает сколько строк было обновленно в последней UPDATE или DELETE инструкции

# проверка измнения внешнего ключа на несуществующее значение в референсе - при включенной поддержке внешних ключей, выдает ошибку
cur.execute('''UPDATE Inventory SET PlaceID = 99 WHERE ItemID == 1''')

# удаление строк из бд
cur.execute('''DELETE FROM Inventory WHERE ItemID == 3''') # инструкция удаляет строку целиком

# проверка удаления первичного ключа который ссылается на внешний ключ в другой таблице - при включенной поддержке внешних ключей, выдает ошибку
cur.execute('''DELETE FROM Places WHERE PlaceID == 2''')



# сохранение изменений в таблице
conn.commit()

conn.close()