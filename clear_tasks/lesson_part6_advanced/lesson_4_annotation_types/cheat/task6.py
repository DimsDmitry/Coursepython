# Задание 6: Функция с несколькими типами
#
# Создайте функцию process_data, которая принимает аргумент типа Union[int, str] и возвращает строку.
# Если передан int, функция должна вернуть его строковое представление, а если str — вернуть его в верхнем регистре.
# Укажите аннотации типов.

from typing import Union

def process_data(data: Union[int, str]) -> str:
    if isinstance(data, int):
        return str(data)