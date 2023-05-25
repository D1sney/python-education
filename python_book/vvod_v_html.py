name = input('Введите ваше имя: ')
file = open(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\test2.txt', 'w', encoding='utf8')
text = f'''<html>
<head>
</head>
<body>
  <center>
    <h1>{name}</h1>
  </center>
  <hr />
'''  
  
text3 = f'''  <hr />
</body>
</html>
'''
file.write(text)
choice = input('Хотите рассказать о себе? ')
while choice == 'да':
    about = input('Введите строку описания ')
    file.write(f'  {about}\n')
    choice = input('Желаете ввести еще одну строку? ')
file.write(text3)


file.close()