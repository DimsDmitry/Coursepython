# Задание 10: Класс с типами
#
# Создайте класс Rectangle, который имеет два атрибута width и height (оба типа float).
# Реализуйте метод area, который возвращает площадь прямоугольника. Укажите аннотации типов.

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height