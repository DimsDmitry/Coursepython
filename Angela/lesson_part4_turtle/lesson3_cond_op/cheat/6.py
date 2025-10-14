# Напиши программу, которая запрашивает время суток и в зависимости от ответа
# "день" - рисует солнце (18-ти конечная звезда с размером стороны 100, угол поворота 100)
# "ночь" - рисует луну (радиус 50, цвет "bisque")

from turtle import *


def day():
    pensize(2)
    color("yellow")
    begin_fill()
    for i in range(18):
        forward(100)
        left(100)
    end_fill()


def night():
    pensize(2)
    color("bisque")
    begin_fill()
    circle(50)
    end_fill()


answer = input("Какое сейчас время суток (день/ночь)?")
speed(0)
if answer == "день":
    day()
if answer == "ночь":
    night()
hideturtle()
exitonclick()
