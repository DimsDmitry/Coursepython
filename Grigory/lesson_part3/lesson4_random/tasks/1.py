# Написать программу, которая с помощью модуля random моделирует
# броски монеты и выводит результаты бросков (орёл или решка) на экран.

from random import *
# вар 1
my_list = ['орёл', 'решка']
shuffle(my_list)
print('Выпало:', my_list[0])

# вариант 2
num = randint(1, 2)
if num == 1:
    res = 'орёл'
else:
    res = 'решка'
print('Выпало:', res)