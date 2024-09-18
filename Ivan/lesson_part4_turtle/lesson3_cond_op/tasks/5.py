# Напиши программу, запрашивающую ввод горящего сигнала светофора («красный», «жёлтый» или «зелёный»)
# и отрисовывающую светофор с этим горящим сигналом.
# Пример в картинке 5-1, 5-2. Параметры светофора в картинке 5-3


from turtle import *

speed(0)
pensize(3)


def red_light_on():
    color("red")
    penup()
    goto(0, 100)
    pendown()
    begin_fill()
    circle(35)
    end_fill()

    color("yellow")
    penup()
    goto(0, 0)
    pendown()
    circle(35)

    color("green")
    penup()
    goto(0, -100)
    pendown()
    circle(35)


def green_light_on():
    color("red")
    penup()
    goto(0, 100)
    pendown()
    circle(35)

    color("yellow")
    penup()
    goto(0, 0)
    pendown()
    circle(35)

    color("green")
    penup()
    goto(0, -100)
    pendown()
    begin_fill()
    circle(35)
    end_fill()


red_light_on()
green_light_on()

# answer = input("Какой горит цвет красный/жёлтый/зелёный?")
# if answer == "красный":
#     red_light_on()
