# Запрограммируй черепашку на рисование квадрата и треугольника. Рисунок должен остаться на экране.
#
# Квадрат:
# 1) Стороны — 150 пикселей.
# 2) Цвет квадрата — зелёный (green).
# Треугольник:
# 1) Сторона — 150 пикселей.
# 2) Цвет треугольника — жёлтый (yellow).
# 3) Размер пера (pensize) для обоих фигур - 2 пикселя.
# 4)* Угол поворота — 120 градусов.

from turtle import *
pensize(2)
speed(0)

begin_fill()
color("green")
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
end_fill()


color("yellow")
begin_fill()
forward(100)
left(120)
forward(100)
left(120)
forward(100)
left(120)
end_fill()
exitonclick()
