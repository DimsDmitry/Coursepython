# Написать программу, которая с помощью модуля random генерирует 10 случайных строк длиной 10 символов,
# состоящих только из строчных латинских букв.
from random import choice


def random_string(alphabet):
    string = ''
    for _ in range(10):
        sym = choice(alphabet)
        string += sym
    return string

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for _ in range(10):
    new_string = random_string(alphabet)
    print(new_string)