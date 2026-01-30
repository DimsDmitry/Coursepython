# Создайте программу, которая рисует дом с крышей, если пользователь вводит «да», и без крыши,
# если пользователь вводит «нет». Параметры дома произвольные.
from turtle import *

color('blue')
pensize(2)
begin_fill()
for i in range(4):
    forward(100)
    left(90)
end_fill()

roof = input('Дому нужна крыша?').lower()
if roof == 'да':
    goto(0, 100)
    color('brown')
    begin_fill()
    for l in range(3):
        forward(100)
        left(120)
    end_fill()

print('Дом готов')

hideturtle()
exitonclick()