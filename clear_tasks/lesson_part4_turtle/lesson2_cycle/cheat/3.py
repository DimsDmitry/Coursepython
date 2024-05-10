# Допиши программу. Она должна рисовать колесо обозрения (см рис.3). Цвет - dark blue, толщина пера - 2

from turtle import *


def triangle():
    pensize(2)
    color("dark blue")
    for i in range(3):
        forward(100)
        left(120)


speed(0)
for i in range(36):
    triangle()
    right(10)
hideturtle()
exitonclick()
