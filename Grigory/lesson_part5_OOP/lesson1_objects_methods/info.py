# Объект - набор свойств и методов, который удобно воспринимать как единое целое
from turtle import *

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

# СВОЙСТВА:
t1.color('red')
t2.color('green')
t3.color('darkblue')

t1.shape('turtle')
t2.shape('circle')
t3.shape('square')

# МЕТОДЫ:
t1.penup()
t2.penup()
t3.penup()

t1.goto(50, 50)
t2.goto(50, -50)
t3.goto(-50, -50)

t1.pendown()
t2.pendown()
t3.pendown()

t1.forward(100)