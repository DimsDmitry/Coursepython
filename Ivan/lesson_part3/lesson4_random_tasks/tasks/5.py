# Написать программу, которая с помощью модуля random генерирует 10 случайных целых чисел в диапазоне
# от 1 до 100 и выводит их на экран.
from random import *

for i in range(10):
    print(f'Число {i+1} - {randint(1, 100)}')