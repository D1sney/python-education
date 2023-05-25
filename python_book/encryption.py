transcription = {'я':'*','а':'%','о':'?','к':'№','у':'"','л':'!','е':')','п':'(','ю':'=','и':'-','г':'>','р':'<','д':':','Я':';','с':'_','м':'+',}

# шифрование файла
file = open(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\transcript.txt', 'r', encoding='UTF-8')
text = file.read()
file.close()
print(text)
newtext = ''
for i in text:
    if i in transcription:
        newtext += transcription[i]
    else:
        newtext += i    
print(newtext)
file = open(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\cipher.txt', 'w', encoding='UTF-8')
file.write(newtext)
file.close()


# расшифровка файла
file = open(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\cipher.txt', 'r', encoding='UTF-8')
text = file.read()
file.close()
print(text)
newtext = ''
for i in text:
    if i in transcription.values():
        for a in transcription:
            if transcription[a] == i:
                newtext += a
    else:
        newtext += i    
print(newtext)
file = open(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\transcript.txt', 'w', encoding='UTF-8')
file.write(newtext)
file.close()

