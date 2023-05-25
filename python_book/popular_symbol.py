stroka = 'hfahfrbvbrwuwob'
letter = []
for i in stroka:
    if i in letter:
        pass
    else:
        letter.append(i)
totals = []+letter
for i in range(len(totals)):
    totals[i]=0
for i in stroka:
    if i in letter:
        totals[letter.index(i)]+=1
print(letter)
print(totals)
big = 0
for i in totals:
    if i > big:
        big = i
print(letter[totals.index(big)])