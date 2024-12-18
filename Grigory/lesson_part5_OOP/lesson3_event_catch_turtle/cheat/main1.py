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
t1 = Turtle()
t1.color('blue')
t1.width(5)
t1.shape('turtle')

t2 = Turtle()
t2.color('green')
t2.width(5)
t2.left(120)
t2.shape('turtle')

t3 = Turtle()
t3.color('red')
t3.width(5)
t3.left(-120)
t3.shape('turtle')


def catch1(x, y):
    t1.penup()
    t1.goto(randint(-100, 100), randint(-100, 100))
    t1.pendown()
    t1.left(randint(0, 180))


def catch2(x, y):
    t2.penup()
    t2.goto(randint(-100, 100), randint(-100, 100))
    t2.pendown()
    t2.left(randint(0, 180))


def catch3(x, y):
    t3.penup()
    t3.goto(randint(-100, 100), randint(-100, 100))
    t3.pendown()
    t3.left(randint(0, 180))


def gameFinished(t1, t2, t3):
    t1_outside = abs(t1.xcor()) > w or abs(t1.ycor()) > h
    t2_outside = abs(t2.xcor()) > w or abs(t2.ycor()) > h
    t3_outside = abs(t3.xcor()) > w or abs(t3.ycor()) > h
    isOutside = t1_outside or t2_outside or t3_outside
    return isOutside


t1.onclick(catch1)
t2.onclick(catch2)
t3.onclick(catch3)

while not gameFinished(t1, t2, t3):
    t1.forward(7)
    t2.forward(7)
    t3.forward(7)
    sleep(0.1)

t1.clear()
t2.clear()
t3.clear()

'''
t1.penup()
t1.goto(-30, 0)
t1.write('Good bye!', font=('Arial', 16, 'bold'))


t2.penup()
t2.goto(-30, 0)
t2.write('Good bye!', font=('Arial', 16, 'bold'))


t3.penup()
t3.goto(-30, 0)
t3.write('Good bye!', font=('Arial', 16, 'bold'))
'''

t1.hideturtle()
t2.hideturtle()
t3.hideturtle()

exitonclick()
