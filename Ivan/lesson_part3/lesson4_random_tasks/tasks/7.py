# Написать программу, которая с помощью модуля random генерирует 10 случайных дат в формате ГГГГ-ММ-ДД
from random import *

result1 = str(randint(1954, 2024))
result2 = str(randint(1, 12))
result3 = str(randint(1, 31))

res = result1 + '-' + result2 + '-' + result3

print(res)