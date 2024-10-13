# Изучи, как перемещаются черепашки на фото 'game2.png' и запрограммируй это движение.
from turtle import *

# черепашка 1
t1 = Turtle()
t1.color('red')
t1.speed(0)
t1.shape('triangle')
t1.penup()
t1.goto(-50, 50)
t1.pendown()

# черепашка 2
t2 = Turtle()
t2.color('blue')
t2.speed(0)
t2.shape('circle')
t2.penup()
t2.goto(-50, -50)
t2.pendown()

# черепашка 3
t3 = Turtle()
t3.color('green')
t3.speed(0)
t3.shape('turtle')
t3.penup()
t3.goto(50, 50)
t3.pendown()

# черепашка 4
t4 = Turtle()
t4.color('yellow')
t4.speed(0)
t4.shape('square')
t4.penup()
t4.goto(50, -50)
t4.pendown()

for i in range(50):
    t1.forward(i * 3)
    t1.left(90)

    t2.forward(i * 2)
    t2.left(90)

    t3.forward(i * 4)
    t3.left(90)

    t4.forward(i * 2)
    t4.left(90)


