from turtle import *

speed(0)


def draw_landscape():
    penup()
    goto(-300, -300)
    pendown()
    color('green', 'yellowgreen')
    begin_fill()
    for i in range(2):
        forward(600)
        left(90)
        forward(200)
        left(90)
    end_fill()


def draw_sky():
    penup()
    goto(-300, -100)
    pendown()
    color('skyblue')
    begin_fill()
    for i in range(2):
        forward(600)
        left(90)
        forward(500)
        left(90)
    end_fill()


def block_flats():
    # многоэтажный дом
    penup()
    goto(-200, -200)
    pendown()
    color('black', 'gray')
    begin_fill()
    for i in range(2):
        forward(100)
        left(90)
        forward(200)
        left(90)
    end_fill()
    pendown()
    window(-175, -175)
    window(-145, -175)
    window(-175, -125)
    window(-145, -125)


def window(x, y):
    # перемещается по указанным координатам
    penup()
    goto(x, y)
    pendown()
    # рисует окно
    color('yellow')
    begin_fill()
    for i in range(4):
        forward(20)
        left(90)
    end_fill()


draw_landscape()
draw_sky()
block_flats()
