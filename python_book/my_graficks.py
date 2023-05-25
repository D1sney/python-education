import turtle

def box(x,y,a,b,counter,color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.pencolor(counter)
    turtle.setheading(0)
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(b)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()

def circle(x,y,radius,counter,color):
    turtle.penup()
    turtle.goto(x,y-radius)   
    turtle.pendown()
    turtle.pencolor(counter)
    turtle.setheading(0)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x,y)

def line(x1,y1,x2,y2,color):
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(x2,y2)
    turtle.penup()

if __name__ == '__main__':
    turtle.speed(0)
    box(100,100,60,200,'red','blue')
    box(-100,-100,100,100,'green','yellow')
    circle(-200,100,50,'brown', 'orange')
    line(-200,100,300,-100,'purple')
    turtle.done()