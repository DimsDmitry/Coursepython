from random import randint, choice
from turtle import *
from time import sleep


def start_race(t, x, y, color):
    """назначает черепашке цвет, форму перемещает её по заданным координатам на исходную"""
    t.color(color)
    t.shape('turtle')
    t.speed(0)
    t.penup()
    t.goto(x, y)


def draw_lines(t):
    """отрисовка разметки"""
    # размещаем на исходной позиции
    t.color('lightgray')
    t.speed(0)
    t.penup()
    x = -200
    y = 200
    t.goto(x, y)
    t.pendown()
    t.right(90)
    # цикл отрисовки
    for i in range(20):
        t.forward(400)
        t.penup()
        x += 20
        t.goto(x, y)
        t.pendown()
    t.left(90)


def check_winner(t1, t2, t3):
    """определяет победителя-черепашку"""
    # сначала узнаем бОльшую координату X
    max_x = max(t1.xcor(), t2.xcor(), t3.xcor())
    # далее узнаем какой из черепашек принадлежит эта координата,
    # функция вернёт соответствующую черепашку
    if t1.xcor() == max_x:
        return t1
    elif t2.xcor() == max_x:
        return t2
    return t3


def dance(t):
    """принимает черепашку-победителя, рисует её победный танец"""
    t.left(randint(0, 90))
    for i in range(8):
        t.penup()
        t.goto(0, 0)
        t.pendown()
        for j in range(32):
            t.forward(j)
            t.left(j/2 + 5)
    t.penup()
    t.goto(0, 0)


def get_rand_color():
    """генерирует случайный цвет для черепашки и возвращает его"""
    color_list = 'cyan red blue black orange green lightblue bisque purple yellow lime magenta'.split()
    return choice(color_list)


# создаём участников гонки
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

# Отрисовка разметки
draw_lines(t1)

# размещаем черепашек на исходную позицию
start_race(t1, -200, 50, 'red')
start_race(t2, -200, 0, 'blue')
start_race(t3, -200, -50, 'green')

finish = 200  # Финишная координата по X

# гонка продолжается до тех пор, пока X-координата одной из черепашек
# меньше указанного значения
while t1.xcor() < finish and t2.xcor() < finish and t3.xcor() < finish:
    t1.forward(randint(2, 7))
    t2.forward(randint(2, 7))
    t3.forward(randint(2, 7))
    # назначаем черепашкам случайный цвет
    t1.color(get_rand_color())
    t2.color(get_rand_color())
    t3.color(get_rand_color())

sleep(2)
# определяем победителя
winner = check_winner(t1, t2, t3)
# победитель танцует
dance(winner)

