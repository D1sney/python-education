import json

file = open(r'C:\Users\ivan3\OneDrive\Рабочий стол\python education\files\group_people.json', 'r')
data = json.load(file)
# print(data)
count = dict()
file.close()
for group in data:
    count[group['id_group']] = 0
    for person in group['people']:
        if person['gender'] == 'Female' and person['year'] > 1977:
            count[group['id_group']] += 1

m = max(count.values())

for key in count:
    if count[key] == m:
        print(key, m)
