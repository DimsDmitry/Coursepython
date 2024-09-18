# Упрости программу. Она должна занимать не более 13-ти строк.

from turtle import *

pensize(2)
speed(0)
color("navy")
size = 10
for i in range(4):
    for _ in range(7):
        circle(size)
        size += 15
    size = 10
    left(90)

hideturtle()
exitonclick()

