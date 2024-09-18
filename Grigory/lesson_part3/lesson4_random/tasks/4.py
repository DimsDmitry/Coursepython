# Написать программу, которая с помощью модуля random генерирует 5 уникальных случайных чисел
# в диапазоне от 1 до 100 и выводит их на экран.
from random import *
mylist = []

for i in range(8):
    mylist.append(randint(1, 100))

print(mylist)