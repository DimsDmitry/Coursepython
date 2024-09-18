# Напишите программу, которая запрашивает размер стороны фигуры, и рисует треугольник,
# если длина стороны больше 100, и квадрат, если длина стороны меньше или равна 100.
# Параметры фигур:
# треугольник: цвет - 'green', размер пера - 2
# квадрат: цвет - 'pink', размер пера - 3
from turtle import *


def triangle(size):
    # рисует треугольник указанного размера
    color('green')
    pensize(2)
    for i in range(3):
        forward(size)
        left(120)


def square(size):
    # рисует квадрат указанного размера
    color('pink')
    pensize(3)
    for i in range(4):
        forward(size)
        left(90)


size = int(input('Введите размер стороны фигуры:'))
if size > 100:
    triangle(size)
else:
    square(size)

exitonclick()
