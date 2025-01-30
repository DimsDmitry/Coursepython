"""Аннотация типов не обеспечивает проверку типов на уровне интерператора.
Она нужна для разработчиков и для более удобного понимания кода
Python поддерживает аннотацию типов для типов данных:
str, int, float, bool, None
Остальные необходимо импортировать"""

a: int = 5

print(a * 2)

a: str = '5'

print(a * 2)

average_count: float = 3.9
print(average_count)

from typing import List

marks: List[int] = [5, 2, 3, 4, 5, 2]
print(marks)
print('\n')
"""АННОТАЦИЯ ФУНКЦИЙ
синтаксис аннотаций работает и для параметров функций.
Мы можем указывать тип возврата с помощью стрелки"""


def do_something(a: int, b: int) -> tuple:
    return a + b, a * b


result1, result2 = do_something(10, 2)
print(result1)
print(result2)

"""Специальные типы"""

from typing import Any, Literal

# Any - неограниченный тип. Совместим со всеми типами, а они - с ним
result: Any = 'Hello!'
print(result)
print('\n')

# Literal - переменная имеет одно из указанных значений
ANIMALS = Literal['cat', 'dog', 'bird', 'flamingo', 'snake']
print(ANIMALS)


def create_pet(name: str, age: int, kind: ANIMALS) -> dict[str, int, ANIMALS]:
    return {'name': name, 'age': age, 'kind': kind}


my_animal = create_pet('Кокос', 2, 'cat')
print(my_animal)
# одно из значений литерального объявления ANIMALS - 'cat', 'dog', 'bird', 'flamingo' или 'snake'

# Union - иногда переменная может обладать свойствами, общими для двух типов
# Это означает, что переменная может иметь два типа данных

from typing import Union, TypedDict


def get_my_temperature() -> Union[int, float]:
    return '36.6'


result = get_my_temperature()
print(result)


# TypedDict

class User(TypedDict):
    login: str
    card_number: Union[str, int]


user1: User = {login: 'Dima123', card_number: '22022002'}
# или можно сделать его инстанс - объект класса
print(user1)

# NoReturn, Final