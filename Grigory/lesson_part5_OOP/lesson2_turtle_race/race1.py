# Запрограммируй черепашьи гонки! пример на фото
from turtle import *
from random import *
from time import sleep

finish = 200


def get_rand_color():
    color_list = 'cyan red blue black orange green lightblue bisque purple yellow lime magenta'.split()
    shuffle(color_list)
    cur_color = color_list[0]
    return cur_color


def draw_lines(t):
    t.pensize(2)
    t.speed(0)
    t.penup()
    x = -200
    y = 200
    t.goto(x, y)
    t.right(90)
    t.pendown()
    color_i = 1
    for i in range(21):
        if color_i == 1:
            t.color('red')
        if color_i == 2:
            t.color('blue')
        if color_i == 3:
            t.color('green')
        color_i += 1
        if color_i > 3:
            color_i = 1
        t.forward(400)
        t.penup()
        x += 20
        t.goto(x, y)
        t.pendown()
    t.left(90)


def start_race(t, x, y, cur_color):
    # настраиваем черепашек на гонку
    t.color(cur_color)
    t.shape('turtle')
    t.speed(9)
    t.penup()
    t.goto(x, y)


def dance(t):
    # танец победившей черепашки
    t.speed(8)
    t.left(randint(0, 90))
    for i in range(8):
        t.penup()
        t.goto(0, 0)
        t.pendown()
        for j in range(32):
            t.forward(j)
            t.left(j / 2 + 5)
    t.penup()
    t.goto(0, 0)


# создаём участников гонки
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

# чертим разметку
draw_lines(t1)
sleep(2)

# начало гонки
start_race(t1, -200, -20, get_rand_color())
start_race(t2, -200, 20, get_rand_color())
start_race(t3, -200, 60, get_rand_color())
sleep(2)

while t1.xcor() < finish and t2.xcor() < finish and t3.xcor() < finish:
    # гонка длится, пока одна из черепашек не достигла финиша
    t1.forward(randint(2, 8))
    t2.forward(randint(2, 8))
    t3.forward(randint(2, 8))
    t1.color(get_rand_color())

max_x = max(t1.xcor(), t2.xcor(), t3.xcor())
if t1.xcor() == max_x:
    dance(t1)
if t2.xcor() == max_x:
    dance(t2)
if t3.xcor() == max_x:
    dance(t3)

exitonclick()
