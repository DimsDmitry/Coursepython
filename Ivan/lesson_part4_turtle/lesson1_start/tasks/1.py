# Создать программу, которая рисует квадрат со стороной 20.
# Обязательные параметры - цвет красный (red), толщина линии - 3
# Рисунок должен остаться на экране
from turtle import *


pensize(3)
color('red')

forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)

exitonclick()
