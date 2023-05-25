import turtle
import random
turtle.speed(0)
turtle.hideturtle()

def square(s1,s2,color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(s1)
        turtle.left(90)
        turtle.forward(s2)
        turtle.left(90)
    turtle.end_fill()


turtle.penup()
turtle.goto(-300,-300)
square(600,600,'black')
square(600, 200,'dim grey')
turtle.forward(80)
square(100,300,'dim grey')
turtle.forward(100)
square(140,550,'dim grey')
turtle.forward(140)
square(80,280,'dim grey')
turtle.forward(80)
square(100,450,'dim grey')
turtle.forward(100)
square(40,320,'dim grey')
turtle.goto(-200,-65)
square(25,25,'pale goldenrod')
turtle.goto(-100,185)
square(25,25,'pale goldenrod')
turtle.goto(-100,145)
square(25,25,'pale goldenrod')
turtle.goto(-25,90)
square(25,25,'pale goldenrod')
turtle.goto(-60,-110)
square(25,25,'pale goldenrod')
turtle.goto(120,85)
square(25,25,'pale goldenrod')

def stars(x1,x2,y1,y2):
    for i in range(random.randint(1,5)):
        turtle.goto(random.randint(x1,x2),random.randint(y1,y2))
        turtle.pendown()
        turtle.dot()
        turtle.penup()

turtle.pencolor('white')
stars(-300,-220,-100,250)
stars(-220,-120,0,250)
stars(20,100,-20,250)
stars(100,200,150,250)
stars(200,240,20,250)
stars(240,300,-100,250)
stars(-300,300,250,300)


turtle.done()