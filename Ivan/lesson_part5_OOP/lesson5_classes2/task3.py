"""Запрограммируй класс Rectangle (прямоугольник):
1) Создай конструктор класса. Он должен создавать прямоугольник со свойствами: длина и ширина (вводятся с клавиатуры).

2) Создай метод, печатающий информацию о фигуре. Он должен выводить данные: «Прямоугольник с длиной _ и шириной _».

3) Создай метод, вычисляющий и возвращающий периметр прямоугольника.

4) Создай метод, вычисляющий и возвращающий площадь прямоугольника.

Запроси с клавиатуры длину и ширину прямоугольника и создай соответствующий экземпляр класса Rectangle.
Напечатай информацию об объекте.
Затем вычисли и напечатай периметр (с пометкой «Его периметр: _») и площадь (с пометкой: «Его площадь: _»).

Оформи всё как в примере ниже:

Введите длину:>? 20
Введите ширину:>? 5
Прямоугольник с длиной 20 и шириной 5
Его периметр: 50
Его площадь: 100
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def print_info(self):
        print(f'Прямоугольник с длиной {self.length} и шириной {self.width}')

    def calc_perimeter(self):
        perimeter = 2 * (self.length + self.width)


a = int(input('Введите длину прямоугольника:'))
b = int(input('Введите ширину прямоугольника:'))
rect1 = Rectangle(a, b)
rect1.print_info()