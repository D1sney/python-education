file = open(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\USA.txt', 'r')
years = file.readlines()
# print(years)
for i in range(len(years)):
    years[i] = int(years[i])
# print(years)

changes = []
for i in range(1,len(years)):
    changes.append(years[i]-years[i-1])
# print(changes)
# print(len(years), len(changes))

sum = 0
for i in changes:
    sum+=i

print(f'Среднегодовое изменение: {sum/len(changes)}\nГод с наибольшем увеличением численности: {1951 + changes.index(max(changes))}\nГод с наименьшем увеличением численности: {1951 + changes.index(min(changes))}')
