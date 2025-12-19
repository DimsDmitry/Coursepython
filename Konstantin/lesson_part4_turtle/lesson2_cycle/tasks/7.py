# Запрограммируй узор. Результат работы должен быть как на картинке.
# После отрисовки изображение должно остаться на экране. Точка начала рисования - (-50, -50)
# Размеры и цвета квадратов:
# 200, 'black'
# 150, 'white'
# 100, 'lavender'
# 50, 'black'


from turtle import *


goto(-50, -50)

def draw_square(length, cur_color):
    """рисует квадрат с указанной стороной и цветом"""
    begin_fill()  # начать заливку

    pensize(2)
    color(cur_color)  # назначить цвет

    for _ in range(4):
        forward(length)
        left(90)

    end_fill()  # закончить заливку

draw_square(200, 'black')
draw_square(150, 'lavender')
draw_square(100, 'white')
draw_square(50, 'black')

color('black')
for _ in range(4):
    forward(200)
    left(90)

hideturtle()
exitonclick()