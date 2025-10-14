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
elif cur_color == 'зелёный':
    star('green')
elif cur_color == 'красный':
    star('red')
elif cur_color == 'коричневый':
    star('brown')
elif cur_color == 'коралловый':
    star('coral')

hideturtle()
exitonclick()
