# Нарисуй солнышко. Количество лучей — 18. Угол поворота — 100. Толщина линии - 3 пикселя. Цвет произвольный


from turtle import *


def sun():
    pensize(3)
    color("yellow")
    speed(0)
    begin_fill()
    for i in range(18):
        forward(150)
        left(100)
    end_fill()


sun()
hideturtle()
exitonclick()
