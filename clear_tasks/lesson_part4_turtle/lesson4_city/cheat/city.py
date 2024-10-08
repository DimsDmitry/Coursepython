from turtle import *


def draw_landscape():
    penup()
    goto(-200, -200)
    pendown()
    color('green', 'yellowgreen')
    begin_fill()
    for i in range(2):
        forward(400)
        left(90)
        forward(100)
        left(90)
    end_fill()


def draw_sky():
    penup()
    goto(-200, -100)
    pendown()
    # color('paleturquoise')
    color('skyblue')
    begin_fill()
    for i in range(2):
        forward(400)
        left(90)
        forward(300)
        left(90)
    end_fill()


def draw_window():
    color('yellow')
    begin_fill()
    for i in range(4):
        forward(20)
        left(90)
    end_fill()


def draw_block_of_flats():
    penup()
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
    penup()
    goto(-145, -145)
    pendown()
    draw_window()
    penup()
    goto(-115, -145)
    pendown()
    draw_window()
    penup()
    goto(-145, -85)
    pendown()
    draw_window()
    penup()
    goto(-115, -85)
    pendown()
    draw_window()
    penup()
    goto(-145, -35)
    pendown()
    draw_window()
    penup()
    goto(-115, -35)
    pendown()
    draw_window()


def draw_sun():
    penup()
    goto(140, 140)
    pendown()
    begin_fill()
    color('orange', 'yellow')
    for i in range(18):
        forward(40)
        left(100)
    end_fill()


def draw_pharmacy():
    penup()
    goto(120, -160)
    pendown()
    color('brown', 'goldenrod')
    begin_fill()
    for i in range(3):
        forward(70)
        left(90)
    end_fill()
    penup()
    goto(140, -110)
    pendown()
    pensize(5)
    color('red')
    forward(15)
    penup()
    goto(150, -118)
    pendown()
    color('red')
    right(90)
    forward(20)
