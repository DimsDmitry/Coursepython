# Задание 5: Поиск максимального значения
#
# Напишите функцию find_max, которая принимает список чисел (тип List[float]) и возвращает
# максимальное значение из этого списка (тип float). Добавьте аннотации типов.

from typing import List


def find_max(numbers: List[float]) -> float:
    return max(numbers)
