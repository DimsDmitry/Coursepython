from turtle import *

pensize(3)
penup()
goto(-100, -100)
pendown()
color('red')
for i in range(4):
    forward(50)
    left(90)
penup()
goto(50, 50)
pendown()
color('purple')
circle(25)

exitonclick()