# Запрограммируй узор. Результат работы должен быть как на картинке.
# После отрисовки изображение должно остаться на экране. Точка начала рисования - (-50, -50)
# Размеры и цвета квадратов:
# 200, 'black'
# 150, 'white'
# 100, 'lavender'
# 50, 'black'


from turtle import *

goto(-50, -50)


def square(length, cur_color):
    pensize(2)
    color(cur_color)
    begin_fill()
    for i in range(4):
        forward(length)
        left(90)
    end_fill()


square(200, 'black')
square(150, 'white')
square(100, 'lavender')
square(50, 'black')
hideturtle()
exitonclick()
