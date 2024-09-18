# Написать программу, которая с помощью модуля random генерирует 10 случайных дат в формате ГГГГ-ММ-ДД
from random import *

year = str(randint(1000, 3000))
month = str(randint(1, 12))
day = str(randint(1, 31))

result = year + '-' + month + '-' + day
print(result)
