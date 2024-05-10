# Написать программу, которая с помощью модуля random генерирует 10 случайных строк длиной 10 символов,
# состоящих только из строчных латинских букв.
from random import *


symbols = 'qwertyuiopasdfghjklzxcvbnm'
string = ''

for a in range(10):
    for i in range(10):
        rand_index = randint(0, len(symbols)-1)
        rand_sym = symbols[rand_index]
        string += rand_sym
    print(f'Сгенерирована строка {a+1}: {string}')
    string = ''