# Задание 9: Фильтрация списка
#
# Напишите функцию filter_even_numbers, которая принимает список целых чисел и возвращает новый список,
# содержащий только четные числа. Укажите аннотации типов.

from typing import List


def filter_even_numbers(numbers: List[int]) -> List[int]:
    return [n for n in numbers if n % 2 == 0]
