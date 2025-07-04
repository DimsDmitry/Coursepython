# Класс с использованием *args и kwargs**: Реализуйте класс Person, который принимает
# имя и возраст через __init__ с использованием *args и **kwargs. Добавьте метод для вывода информации о человеке.


class Person:
    def __init__(self, *args, **kwargs):
        # Проверяем, переданы ли имя и возраст
        if len(args) > 0:
            self.name = args[0]
        else:
            self.name = kwargs.get('name', 'Неизвестно')

        if len(args) > 1:
            self.age = args[1]
        else:
            self.age = kwargs.get('age', 'Неизвестно')

    def display_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}")

# Пример использования
person1 = Person("Алексей", 30)
person2 = Person(name="Мария", age=25)

person1.display_info()  # Вывод: Имя: Алексей, Возраст: 30
person2.display_info()  # Вывод: Имя: Мария, Возраст: 25


# ▎Объяснение кода:
#
# 1. Конструктор __init__:
#
#    • Использует *args для получения позиционных аргументов (в данном случае, имя и возраст).
#
#    • Если имя и возраст не переданы через args, они могут быть указаны через **kwargs.
#
#    • Если ни одно из значений не было передано, по умолчанию устанавливается 'Неизвестно'.
#
# 2. Метод display_info:
#
#    • Выводит информацию о человеке в читаемом формате.
#
# ▎Примеры использования:
#
# • Создание объектов класса Person с использованием как позиционных аргументов, так и именованных.
#
# • Вызов метода для отображения информации о каждом человеке.