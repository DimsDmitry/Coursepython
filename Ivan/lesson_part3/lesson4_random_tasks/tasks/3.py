# Написать программу, которая с помощью модуля random генерирует случайный пароль длиной 8 символов,
# состоящий только из строчных латинских букв и цифр.
from random import *


symbols = 'qwertyuiopasdfghjklzxcvbnm0123456789'
password = ''

for i in range(8):
    rand_index = randint(0, len(symbols)-1)
    rand_sym = symbols[rand_index]
    password += rand_sym

print('Сгенерирован пароль:', password)