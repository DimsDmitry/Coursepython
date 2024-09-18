# Написать программу, которая с помощью модуля random генерирует случайный пароль длиной 8 символов,
# состоящий только из строчных латинских букв и цифр.
from random import *

alphabet = 'abcdefghiklmnopqrstvwxyz0123456789'
result = ''
for i in range(8):
    index = randint(0, len(alphabet)-1)
    sym = alphabet[index]
    result += sym
print(result)

