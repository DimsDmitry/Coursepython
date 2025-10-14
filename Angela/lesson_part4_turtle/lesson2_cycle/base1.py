from turtle import *

speed(0)
color('orange')
begin_fill()
for i in range(40):
    for i in range(4):
        forward(100)
        left(90)
    left(10)
end_fill()

exitonclick()