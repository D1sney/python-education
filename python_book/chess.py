import turtle
turtle.speed(0)

def square(s1,color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(s1)
        turtle.left(90)
    turtle.end_fill()

def chess(checks_x,checks_y,wall):
    for m in range(checks_y):
        turtle.pendown()
        if m%2==0:
            for i in range(checks_x):
                if i%2!=0:
                    square(wall,'white')
                elif i%2==0:
                    square(wall,'black')
                turtle.forward(wall)
        elif m%2!=0:
            for i in range(checks_x):
                if i%2!=0:
                    square(wall,'black')
                elif i%2==0:
                    square(wall,'white')
                turtle.forward(wall)
        turtle.penup()
        turtle.left(180)
        turtle.forward(wall*checks_x)
        turtle.left(90)
        turtle.forward(wall)
        turtle.left(90)

if __name__ =='__main__':
    chess(8,8,30)
    turtle.done()
