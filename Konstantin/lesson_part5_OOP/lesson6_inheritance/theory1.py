# язык python - объектно ориентированный. каждая переменная - объект класса
# a = 10
# print(type(a))


# напишем класс Car - машина

class Car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year
        # атрибуты (свойства) - это переменные внутри класса. Они перечисляются внутри __init__

    def print_info(self):
        """вывести информацию об экземпляре класса"""
        print(f'Марка машины: {self.mark}')
        print(f'Модель машины: {self.model}')
        print(f'Год выпуска: {self.year}\n')


# создадим класс Truck на основе класса Car, чтобы расширить его новыми свойствами и методами
# Car - суперкласс/родительский класс, Truck - подкласс/дочерний класс/класс-наследник
class Truck(Car):
    def __init__(self, mark, model, year, body_size):
        super().__init__(mark, model, year)
        self.body_size = body_size

    def print_info(self):
        """вывести информацию об экземпляре класса"""
        print(f'Марка машины: {self.mark}')
        print(f'Модель машины: {self.model}')
        print(f'Год выпуска: {self.year}')
        print(f'Объём кузова: {self.body_size} кубических метров\n')


# полиморфизм - способность объектов с одинаковым названием, находясь
# в разных классах/функциях и тд, выполнять разные действия

class Taxi(Car):
    """наследник класса Car для машин такси"""

    def advert(self):
        print(f'Прокатись на нашем прекрасном {self.mark} {self.model} {self.year} года выпуска!')
        print(f'Стоимость - всего 50р/километр!\n')


my_car = Car('Toyota', 'AE86', 1985)
my_car.print_info()

work_car = Truck('КАМАЗ', 6520, 2015, 10)
work_car.print_info()

taxi_car = Taxi('Hyundai', 'Solaris', 2020)
taxi_car.print_info()
taxi_car.advert()


# множественное наследование

class A:
    def func_a(self):
        print('Класс А')


class B:
    def func_b(self):
        print('Класс Б')


class C(A, B):
    def func_c(self):
        print('Это дочерний класс А и Б')


object_c = C()
object_c.func_a()
object_c.func_b()



