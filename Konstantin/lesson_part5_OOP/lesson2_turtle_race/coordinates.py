from turtle import *
from time import sleep

t1 = Turtle()

for i in range(10):
    t1.forward(10)
    t1.left(5)
    sleep(1)
    print(f'X: {t1.xcor()}')
    print(f'Y: {t1.ycor()}\n')


