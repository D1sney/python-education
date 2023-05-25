import turtle
import random
import time

#оптимальная сила для размеров окна
OPTIMAL_FORCE = 32
#оптимальное значение координат для цели
OPTIMAL_RANDOM = 225

turtle.setup(670,670)
hits = 0


level=turtle.numinput('Выберите уровень сложности', 'от одного до трех', minval=1, maxval=3)
if level < 1.5:
    lengh = 35
    color = 'cyan'
    turtle.bgcolor(color)
    levelup = 'Easy'
elif level >= 1.5 and level <2.5:
    lengh = 25
    color = 'blue'
    turtle.bgcolor(color)
    levelup = 'Medium'
elif level >= 2.5:
    lengh = 15
    color = 'purple'
    turtle.bgcolor(color)
    level ='Hard'

for i in 'qwert':
    otstup1 = 0
    otstup2 = 12
    turtle.speed(0)
    Rx = random.randint(-OPTIMAL_RANDOM, OPTIMAL_RANDOM)
    Ry = random.randint(-OPTIMAL_RANDOM, OPTIMAL_RANDOM)
    turtle.penup()
    turtle.goto(Rx,Ry)
    turtle.forward(lengh)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(lengh)
    
    
    for i in 'qwe':
        turtle.begin_fill()
        turtle.fillcolor('white')
        for x in 'qwer':
            turtle.left(90)
            turtle.forward(lengh*2 - otstup1)
        turtle.end_fill()
        turtle.penup()
        turtle.left(90)
        turtle.forward(lengh/6)
        turtle.left(90)
        turtle.forward(lengh/6)
        turtle.pendown()
        turtle.setheading(90)
        turtle.begin_fill()
        turtle.fillcolor('red')
        for i in 'qwer':
            turtle.left(90)
            turtle.forward(lengh*2/12*(otstup2-2))
        turtle.end_fill()
        turtle.penup()
        turtle.left(90)
        turtle.forward(lengh/6)
        turtle.left(90)
        turtle.forward(lengh/6)
        turtle.pendown()
        turtle.setheading(90)

        otstup2 -= 4
        otstup1 += (lengh/3)*2
        
    
    turtle.fillcolor('black')  
    turtle.penup()
    turtle.goto(0,0)
    turtle.speed(1)
    Force = turtle.numinput('Введите силу выстрела', 'от 0 до 10', minval=0, maxval=10)
    Angle = turtle.numinput('Введите угод выстрела', 'от 0 до 360', minval=0, maxval=360)
    turtle.pendown()
    turtle.setheading(Angle)
    turtle.forward(Force*OPTIMAL_FORCE)

    
    if (turtle.xcor() <= Rx+lengh/6 and
    turtle.xcor() >= Rx-lengh/6 and
    turtle.ycor() <= Ry+lengh/6 and
    turtle.ycor() >= Ry-lengh/6):
        print('В яблочко!!!')
        for x in 'qwertyqwertyqwertyqwertyqwertyqwerty':
            turtle.bgcolor('orange')
            time.sleep(0.1)
            turtle.bgcolor('yellow')
        hits += 1
        turtle.bgcolor('green')
        time.sleep(1)
    elif (turtle.xcor() <= Rx+lengh and
    turtle.xcor() >= Rx-lengh and
    turtle.ycor() <= Ry+lengh and
    turtle.ycor() >= Ry-lengh):
        print('Попал')
        for x in 'qwertyqwertyqwerty':
            turtle.bgcolor('yellow')
            time.sleep(0.1)
            turtle.bgcolor('green')
        hits += 1
        turtle.bgcolor('green')
        time.sleep(1)
    else:
        print('Мимо')
        turtle.bgcolor('red')
        
    time.sleep(2)
    turtle.reset()
    turtle.bgcolor(color)

turtle.hideturtle()
if hits<4:
    turtle.pencolor('red')
else:
    turtle.pencolor('green')
turtle.write(f'Ты попал {hits}/5 \nСложность: {levelup:^10}')    
print(f'Ты попал {hits}/5')    
    
turtle.done()