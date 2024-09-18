# Напиши программу, которая принимает один из цветов: розовый, зелёный, красный, коричневый, коралловый (coral)
# и рисует пятиконечную звезду (размер стороны 100, угол поворота 144) указанного цвета


from turtle import *


def star(c_color):
    pensize(2)
    color(c_color)
    begin_fill()
    for i in range(5):
        forward(100)
        left(144)
    end_fill()


cur_color = input('Введите цвет:').lower()
if cur_color == 'розовый':
    star('pink')
if cur_color == 'зелёный' or cur_color == 'зеленый':
    star('green')
if cur_color == 'красный':
    star('red')
if cur_color == 'красный':
    star('red')


hideturtle()
exitonclick()
