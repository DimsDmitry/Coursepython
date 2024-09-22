# Напиши программу, запрашивающую ввод горящего сигнала светофора («красный», «жёлтый» или «зелёный»)
# и отрисовывающую светофор с этим горящим сигналом.
# Пример в картинке 5-1, 5-2. Параметры светофора в картинке 5-3


from turtle import *

speed(0)


def red_light_on():
    color("red")
    penup()
    goto(0, 100)
    pendown()
    begin_fill()
    circle(35)
    end_fill()


def red_light_off():
    color("red")
    penup()
    goto(0, 100)
    pendown()
    circle(35)


def yellow_light_on():
    color("yellow")
    penup()
    goto(0, 0)
    pendown()
    begin_fill()
    circle(35)
    end_fill()


def yellow_light_off():
    color("yellow")
    penup()
    goto(0, 0)
    pendown()
    circle(35)


def green_light_on():
    color("green")
    penup()
    goto(0, -100)
    pendown()
    begin_fill()
    circle(35)
    end_fill()


def green_light_off():
    color("green")
    penup()
    goto(0, -100)
    pendown()
    circle(35)


answer = input("Какой горит цвет красный/жёлтый/зелёный?")
if answer == "красный":
    red_light_on()
    yellow_light_off()
    green_light_off()
if answer == "жёлтый":
    red_light_off()
    yellow_light_on()
    green_light_off()
if answer == "зелёный":
    red_light_off()
    yellow_light_off()
    green_light_on()
hideturtle()
exitonclick()
