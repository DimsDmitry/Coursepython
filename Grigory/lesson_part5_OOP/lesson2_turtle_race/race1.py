# Запрограммируй черепашьи гонки! пример на фото
from turtle import *
from random import randint
from time import sleep

finish = 200


def draw_lines(t):
    t.color('lightgray')
    t.pensize(2)
    t.speed(0)
    t.penup()
    x = -200
    y = 200
    t.goto(x, y)
    t.right(90)
    t.pendown()
    for i in range(21):
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
start_race(t1, -200, -20, 'red')
start_race(t2, -200, 20, 'blue')
start_race(t3, -200, 60, 'green')
sleep(2)

while t1.xcor() < finish and t2.xcor() < finish and t3.xcor() < finish:
    # гонка длится, пока одна из черепашек не достигла финиша
    t1.forward(randint(2, 8))
    t2.forward(randint(2, 8))
    t3.forward(randint(2, 8))

max_x = max(t1.xcor(), t2.xcor(), t3.xcor())
if t1.xcor() == max_x:
    dance(t1)
if t2.xcor() == max_x:
    dance(t2)
if t3.xcor() == max_x:
    dance(t3)

exitonclick()
