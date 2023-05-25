file = open(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\transcript.txt', 'r', encoding='UTF-8')
text = file.read()
file.close()
words = text.split()
clear_words = []
for i in words:
    clear_words.append(i.rstrip('.,?!').lower())
print(clear_words)

count_words = {}
count_words = count_words.fromkeys(set(clear_words), 0)

for i in clear_words:
    count_words[i] += 1

for i in count_words:
    print(i, count_words[i])