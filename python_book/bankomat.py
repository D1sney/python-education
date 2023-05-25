balance = 0
W=0


while W<1 :
    sum=float(input('Какую сумму вы хотите внести? '))
    if sum>=1 and sum/1==sum//1:

        while balance<sum:   
            x = float(input(f'Внесите сумму {sum:.0f} рублей '))
            if x==1 or x==2 or x==5 or x==10 or x==50 or x==100 or x==200 or x==500 or x==1000 or x==2000 or x==5000:
                balance+=x
            else:
                print('Такие платежные саредства не принимаются')
        print(f'Вы внесли сумму в размере {balance:.0f}')

        while W<1:
            y=input(f'Положить данную сумму на счет?\nВведите \"да\", \"нет\"\nИли если вы хотите положить только {sum:.0f} и получить сдачу обратно?\nВведите \"1\"')
            if y =='да':
                print(f'Ваш баланс пополнен на {balance:.0f}')
                W+=1
            elif y=='1':
                print(f'Ваш баланс пополнен на {sum:.0f}\nЗаберите {balance-sum:.0f}')
                W+=1
            elif y=='нет':
                print(f'Заберите {balance:.0f}')
                W+=1



