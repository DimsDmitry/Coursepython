from turtle import *

speed(0)


def draw_landscape():
    # отрисовка земли
    penup()
    goto(-300, -300)
    pendown()
    color('green', 'yellowgreen')
    begin_fill()
    for i in range(2):
        forward(600)
        left(90)
        forward(150)
        left(90)
    end_fill()


def draw_sky():
    # отрисовка неба
    penup()
    goto(-300, -150)
    pendown()
    color('skyblue')
    begin_fill()
    for i in range(2):
        forward(600)
        left(90)
        forward(600)
        left(90)
    end_fill()


def draw_block_flats():
    # отрисовка дома
    goto(-170, -170)
    pendown()
    color('black', 'gray')
    begin_fill()
    for i in range(2):
        forward(100)
        left(90)
        forward(200)
        left(90)
    end_fill()


draw_sky()
draw_landscape()
draw_block_flats()
