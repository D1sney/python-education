import random
def pravila(x,k):
    if (x=='ножницы' and k==3) or (x=='камень' and k==2) or (x=='бумага' and k==1):
        return True
    elif (x=='ножницы' and k==2) or (x=='камень' and k==1) or (x=='бумага' and k==3):
        return 'ничья'
    else:
        return False

siu=1
while siu==1:    
    x=input('выберите: камень, ножницы или бумага? ')
    k=random.randint(1,3)
    if k==1:
        print('компьютнер выбрал камень')
    elif k==2:
        print('комрьютер выбрал ножницы')
    elif k==3:
        print('компьютер выбрал бумагу')

    if pravila(x,k) == True:
        print('вы победили!!!')
        siu =0  
    elif pravila(x,k) =='ничья':
        print('ньчья!!! надо переиграть!')
    else:
        print('вы проиграли!!!')
        siu=0