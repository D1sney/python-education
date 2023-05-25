def is_prime(x):
    t=0
    for i in range(2,x):
        if x%i==0:
           t+=1
    if x==2 or t==0:
        return 'prostoe'
    else:
        return 'neprostoe'    

        
x = int(input('Введите число: '))
spisok = []
for i in range(2,x+1):
    spisok.append(i)

for i in spisok:      
    if is_prime(i) == 'prostoe':
        print(i,end=' ')
