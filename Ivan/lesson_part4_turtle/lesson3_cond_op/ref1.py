from turtle import *


def speed_ok():
    color("green")
    begin_fill()
    circle(50)
    end_fill()


def speed_over():
    color("red")
    penup()
    goto(0, -70)
    pendown()
    begin_fill()
    circle(18)
    end_fill()

    penup()
    goto(-10, -10)
    pendown()
    begin_fill()
    forward(20)
    left(80)
    forward(100)
    left(100)
    forward(55)
    left(100)
    forward(100)
    end_fill()


speed = int(input("Введите скорость транспорта:"))
if speed <= 60:
    speed_ok()
if speed > 60:
    speed_over()
hideturtle()
exitonclick()
