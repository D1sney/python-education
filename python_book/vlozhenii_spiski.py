import random

values = [[[5]],
          [[3,4,3,2], [5,7,8], [2]],
          [[3,5], [0]]]

for row in range(len(values)):
    for value in range(len(values[row])):
        for i in range(len(values[row] [value])):
            values [row] [value] [i] = random.randint(1,100)

for row in values:
    for value in row:
        print(value)

print(values)