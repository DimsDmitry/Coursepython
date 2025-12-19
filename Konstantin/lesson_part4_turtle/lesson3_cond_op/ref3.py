from turtle import *


def square():
    for _ in range(4):
        forward(50)
        left(90)

choice = input('Что нарисовать? Квадрат или круг? (1/2)')
if choice == '1':
    square()
elif choice == '2':
    circle(50)
else:
    print('Действие не выбрано')

hideturtle()
exitonclick()
