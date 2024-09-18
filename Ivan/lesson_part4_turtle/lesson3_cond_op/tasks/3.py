# Создайте программу, которая рисует дом с крышей, если пользователь вводит «да», и без крыши,
# если пользователь вводит «нет». Параметры дома произвольные.
from turtle import *


def house():
    # рисует дом без крыши
    color('brown')
    pensize(4)
    begin_fill()
    for i in range(4):
        forward(100)
        left(90)
    end_fill()
    goto(0, 100)


def roof():
    # рисует крышу для дома
    color('red')
    pensize(4)
    begin_fill()
    for i in range(3):
        forward(100)
        left(120)
    end_fill()


answer = input('Рисуем дом с крышей? да/нет').lower()
if answer == 'да':
    house()
    roof()
else:
    house()
exitonclick()
