# Написать программу, которая с помощью модуля random генерирует 10 случайных строк длиной 10 символов,
# состоящих только из строчных латинских букв.
from random import *


alphabet = 'abcdefghiklmnopqrstvwxyz'
for i in range(10):
    result = ''
    for a in range(10):
        index = randint(0, len(alphabet)-1)
        sym = alphabet[index]
        result += sym
    print(result)