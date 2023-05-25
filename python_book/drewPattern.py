import turtle

def square(s1,s2):
    for i in range(2):
        turtle.forward(s1)
        turtle.left(90)
        turtle.forward(s2)
        turtle.left(90)



def drawPattern(x,y):
    square(x,y)
    start_x=turtle.xcor()
    start_y=turtle.ycor()
    turtle.goto(start_x+x,start_y+y)
    turtle.left(180)
    turtle.forward(x)
    turtle.goto(start_x+x,start_y)
    turtle.penup()
    turtle.goto(start_x+x/8,start_y+y/8)
    turtle.setheading(0)
    turtle.pendown()
    square(x/8*6,y/8*6)
    turtle.goto(start_x+x/4,start_y+y/4)
    turtle.begin_fill()
    square(x/8*4,y/8*4)
    turtle.end_fill()
    turtle.setheading(0)
    turtle.forward(x/4)
    turtle.right(90)
    turtle.forward(y/4)
    turtle.left(180)
    turtle.forward(y)
    turtle.left(90)
    turtle.forward(x/2)
    turtle.left(90)
    turtle.forward(y/2)
    turtle.left(90)
    turtle.forward(x)


if __name__ == '__main__':
    turtle.penup()
    turtle.goto(-400,-100)
    turtle.pendown()
    drawPattern(180,350)
    turtle.done()
    
