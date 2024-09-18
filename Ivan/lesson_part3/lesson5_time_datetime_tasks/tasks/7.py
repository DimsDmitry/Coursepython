'''Напиши программу, которая будет принимать на ввод значения времени и выводить в соответствующем формате

Пример:
Часы: >? 23
Мин: >? 12
Сек: >? 29
23:12:29
'''
from datetime import *
hours = int(input('Часы:'))
mins = int(input('Мин:'))
seconds = int(input('Сек:'))

result = time(hours, mins, seconds)
print(result)