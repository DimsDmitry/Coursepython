# Задание 4: Список квадратов
#
# Создайте функцию squares, которая принимает список целых чисел и возвращает новый список,
# содержащий квадраты этих чисел. Используйте аннотации типов.

from typing import List


def squares(numbers: List[int]) -> List[int]:
    return [n ** 2 for n in numbers]
