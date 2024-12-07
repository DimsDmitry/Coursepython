# Создайте класс Shape (геометрическая фигура) со свойствами name и color (название и цвет).
# У этого класса должны быть три подкласса – Circle (окружность), Rectangle (прямоугольник), и Triangle (треугольник).
# Каждый подкласс наследует атрибут color и методdescribe() родительского класса Shape,
# и при этом имеет дополнительные свойства и методы:
#
# Circle – атрибут radius и метод area() для вычисления площади.
# Rectangle – атрибуты length и width, свой метод area().
# Triangle – атрибуты base и height (основание и высота), собственный метод area().

class Shape:
    def __init__(self, color):
        self.color = color

    def describe(self):
        print(f"Это геометрическая фигура, цвет - {self.color}.")


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def describe(self):
        super().describe()
        print(f"Это окружность. Радиус - {self.radius} см, цвет - {self.color}.")


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def describe(self):
        super().describe()
        print(f"Это {self.color} прямоугольник. Длина - {self.length} см, ширина - {self.width} см.")


class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def describe(self):
        super().describe()
        print(f"Это {self.color} треугольник с основанием {self.base} см и высотой {self.height} см.")