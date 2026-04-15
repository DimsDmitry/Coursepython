from turtle import *
from time import sleep
from random import randint


t = Turtle()
t.color('red')
t.penup()
t.shape('turtle')
t.speed(10)
t.points = 0  # кол-во очков

w = 200
h = 200

def rand_move():
   t.goto(randint(-w, w), randint(-h, h))

def catch(x, y):
    t.points += 1
    t.write('Поймал!', font=('Arial', 20, 'normal'))
    rand_move()

# onclick - при нажатии на объект t вызвать функцию, переданную в скобках
t.onclick(catch)

while t.points < 3:
   sleep(1.5)
   rand_move()

t.write('Победа!', font=('Arial', 20, 'bold'))
t.hideturtle()

