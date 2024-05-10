# Напиши программу, которая нарисует 4 круга радиусом 50 друг на друге по очереди, следующих цветов:
# розовый ("pink")
# оранжевый ("orange")
# жёлтый ("yellow")
# светло-зелёный ("lime")
#
# Рисунок должен остаться на экране


from turtle import *


pensize(10)
color("pink")
circle(50)
color("orange")
circle(50)
color("yellow")
circle(50)
color("lime")
circle(50)
exitonclick()
