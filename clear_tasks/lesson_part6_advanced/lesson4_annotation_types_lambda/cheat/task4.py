# Задание 4: Список квадратов
#
# Создайте функцию squares, которая принимает список целых чисел и возвращает новый список,
# содержащий квадраты этих чисел. Используйте аннотации типов.

from typing import List


# решение 1:

def squares(numbers: List[int]) -> List[int]:
    return [n ** 2 for n in numbers]


# решение 2:

def squares(numbers: List[int]) -> List[int]:
    return list(map(lambda num: num ** 2, numbers))


res = squares([2, 3, 5, 0, 9])
print(res)
