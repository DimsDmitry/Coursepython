# Напиши программу, которая принимает один из цветов: розовый, зелёный, красный, коричневый, коралловый (coral)
# и рисует пятиконечную звезду (размер стороны 100, угол поворота 144) указанного цвета


from turtle import *
from random import choice


def star(c_color):
    pensize(2)
    color(c_color)
    begin_fill()
    for i in range(5):
        forward(100)
        left(144)
    end_fill()


print('Список доступных цветов:\n1 - розовый\n2 - зелёный\n3 - красный\n4 - коричневый\n5 - коралловый\n6 - случайный')
index_color = int(input('Введите номер цвета:').lower())
color_list = 'pink green red brown coral'.split()
try:
    draw_color = color_list[index_color-1]
except IndexError:
    if index_color == 6:
        draw_color = choice(color_list)
    else:
        print('Номер цвета не распознан! Назначим вам голубой')
        draw_color = 'blue'

star(draw_color)

hideturtle()
exitonclick()
