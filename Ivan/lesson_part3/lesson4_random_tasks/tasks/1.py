# Написать программу, которая с помощью модуля random моделирует
# броски монеты и выводит результаты бросков (орёл или решка) на экран.
from random import *

# results = ['орёл', 'решка']
# res = randint(0, 1)
#
# print('Результат:', results[res])

results = ['орёл', 'решка']
shuffle(results)

print('Результат:', results[0])