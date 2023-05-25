import pickle

# запись объектов в файлы
# myobject = 5
# file = open(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\mydata.dat', 'ab')
# pickle.dump(myobject, file)
# file.close()

# чтение объектов из файлов
file = open(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\mydata.dat', 'rb')
loadobject = pickle.load(file)
loadobject2 = pickle.load(file)
# loadobject3 = pickle.load(file) # если попытаться загрузить объект из пустого файла, или уже полностью прочитанного, то вылезет ошибка 
file.close()
print(loadobject, loadobject2)

# консервация и расконсервация объектов в переменные
a = [5,6,6,7]
b = pickle.dumps(a)
print(a, b)
c = pickle.loads(b)
print(c)