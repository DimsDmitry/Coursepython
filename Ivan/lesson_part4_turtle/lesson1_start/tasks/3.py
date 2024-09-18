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
color('green')
pensize(2)

forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)