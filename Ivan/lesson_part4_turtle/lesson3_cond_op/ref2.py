from turtle import *


def fence(color_f):
    color(color_f)
    pensize(3)
    penup()
    goto(-215, 0)
    pendown()
    for i in range(4):
        left(90)
        forward(50)
        right(90)
        forward(25)
        left(90)
        forward(50)
        right(90)
        forward(25)
        right(90)
        forward(50)
        left(90)
        forward(25)
        right(90)
        forward(50)
        left(90)
        forward(25)


answer = input("Введи корпус: главный корпус/приёмная жителей")
if answer == "главный корпус":
    fence("blue")
if answer == "приёмная жителей":
    fence("green")
hideturtle()
exitonclick()
