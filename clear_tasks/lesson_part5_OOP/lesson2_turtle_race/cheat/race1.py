from turtle import *
from time import sleep
from random import *


def get_rand_color():
    # возвращает рандомный цвет из списка
    color_list = 'cyan red blue black orange green lightblue bisque purple yellow lime magenta'.split()
    shuffle(color_list)
    random_color = color_list[0]
    return random_color


def draw_lines(t):
    # рисуем разметку поля
    t.speed(8)
    t.penup()
    x = -200
    y = 200
    t.goto(x, y)
    t.right(90)
    t.pendown()
    color_i = 1
    for i in range(20):
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


def start_race(t, x, y, c_color):
    """функция для назначения черепашке цвета и размещения на старт"""
    t.color(c_color)
    t.shape('turtle')
    t.speed(10)
    t.penup()
    t.goto(x, y)


def dance(t):
    """танец победившей черепашки"""
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

# начало гонки
draw_lines(t1)

sleep(1)

start_race(t1, -200, -20, get_rand_color())
start_race(t2, -200, 20, get_rand_color())
start_race(t3, -200, 60, get_rand_color())

finish = 200  # финишная координата x

sleep(2)

while t1.xcor() < finish and t2.xcor() < finish and t3.xcor() < finish:
    # гонка длится, пока одна из черепашек не финиширует
    t1.forward(randint(2, 7))
    t2.forward(randint(2, 7))
    t3.forward(randint(2, 7))
    t1.color(get_rand_color())
    t2.color(get_rand_color())
    t3.color(get_rand_color())

max_x = max(t1.xcor(), t2.xcor(), t3.xcor())

sleep(2)

if t1.xcor() == max_x:
    dance(t1)
if t2.xcor() == max_x:
    dance(t2)
if t3.xcor() == max_x:
    dance(t3)
