from turtle import *


goto(-50, -50)

color('black', 'red')  # первый цвет обводка, второй - заливка

pensize(5)
begin_fill()

for _ in range(4):
    forward(200)
    left(90)
end_fill()

hideturtle()
exitonclick()