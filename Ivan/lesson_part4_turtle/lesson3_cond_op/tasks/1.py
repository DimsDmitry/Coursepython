# Создайте программу, которая рисует квадрат, если пользователь вводит «квадрат»,
# и круг, если пользователь вводит «круг».
# Параметры фигур: размеры любые
# квадрат: цвет - 'red', размер пера - 2
# круг: цвет - 'green', размер пера - 3
from turtle import *


def square():
    pensize(2)
    color('red')
    for i in range(4):
        forward(100)
        left(90)


def draw_circle():
    pensize(3)
    color('green')
    circle(50)


answer = input('Какую фигуру нарисовать?').lower()
if answer == 'квадрат':
    square()
else:
    draw_circle()

exitonclick()