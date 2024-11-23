# напиши игру "поймай черепашку". Три черепашки появляются на экране и начинают двигаться в разные стороны экрана,
# стремясь дойти до его края. Если одна из них достигает цели, игра закончена. Если пользователь кликает по черепашке,
# она поворачивается на случайный угол и откидывается назад на произвольное количество шагов.
# Победа - пользователь продержался 30 (или меньше, по желанию) секунд, поражение - одна из черепашек дошла до края
# Пример - см фото


from turtle import *
from random import randint
from time import sleep

w = 200
h = 200


# функции, отвечающие за поимку черепашек
def catch1(x, y):
    """черепашка 1 поймана"""
    t1.penup()
    t1.goto(randint(-100, 100), randint(-100, 100))
    t1.pendown()
    t1.left(randint(0, 180))


def catch2(x, y):
    """черепашка 2 поймана"""
    t2.penup()
    t2.goto(randint(-100, 100), randint(-100, 100))
    t2.pendown()
    t2.left(randint(0, 180))


def catch3(x, y):
    """черепашка 3 поймана"""
    t3.penup()
    t3.goto(randint(-100, 100), randint(-100, 100))
    t3.pendown()
    t3.left(randint(0, 180))


def divide():
    """рисует рамку для игрового поля"""
    t4 = Turtle()
    t4.speed(0)
    t4.pensize(3)
    t4.penup()
    t4.goto(-200, -200)
    t4.pendown()
    for i in range(4):
        t4.forward(400)
        t4.left(90)
    t4.hideturtle()


def stop_game(t1, t2, t3):
    """возвращает False, если все черепашки в границах окна, True - если одна из черепашек достигла их"""
    t1_out = abs(t1.xcor()) > w or abs(t1.ycor()) > h
    t2_out = abs(t2.xcor()) > w or abs(t2.ycor()) > h
    t3_out = abs(t3.xcor()) > w or abs(t3.ycor()) > h
    out = t1_out or t2_out or t3_out
    return out

# создаём черепашек
t1 = Turtle()
t1.color('green')
t1.shape('turtle')

t2 = Turtle()
t2.color('red')
t2.shape('turtle')
t2.left(120)

t3 = Turtle()
t3.color('blue')
t3.shape('turtle')
t3.left(-120)

sleep(1)

divide()

sleep(1)
# подключаем обработку событий
t1.onclick(catch1)
t2.onclick(catch2)
t3.onclick(catch3)

while not stop_game(t1, t2, t3):
    t1.forward(7)
    t2.forward(7)
    t3.forward(7)
    sleep(0.1)

exitonclick()
