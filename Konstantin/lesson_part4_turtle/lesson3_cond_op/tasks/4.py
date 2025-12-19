# Напиши программу, которая принимает один из цветов: розовый, зелёный, красный, коричневый, коралловый (coral)
# и рисует пятиконечную звезду (размер стороны 100, угол поворота 144) указанного цвета


from turtle import *


def star(c_color):
    pensize(2)



cur_color = input('Введите цвет:').lower()
if cur_color == 'розовый':
    star('pink')


hideturtle()
exitonclick()
