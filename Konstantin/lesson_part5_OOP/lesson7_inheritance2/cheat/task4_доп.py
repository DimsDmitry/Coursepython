# ПЕРЕД ВЫПОЛНЕНИЕМ ЗАДАЧИ НЕОБХОДИМО ОЗНАКОМИТЬСЯ С ТЕМОЙ "СЛОВАРИ", "ИНКАПСУЛЯЦИЯ" И "ДЕКОРАТОРЫ"
#
# Для военной игры-стратегии нужно написать класс Soldier (солдат).
# Класс имеет атрибуты name, rank и service_number (имя, воинское звание, порядковый номер),
# причем звание и номер – приватные свойства.
#
# Напишите методы для:
#
# получения воинского звания;
# подтверждения порядкового номера;
# повышения в звании;
# понижения в звании.
# Кроме того, нужно создать декоратор для вывода информации о персонаже.
#
# Пример использования:
#
# soldier1 = Soldier("Иван Сусанин", "рядовой", "12345")
# soldier1.get_rank()
# soldier1.promote()
# soldier1.demote()
#
# Вывод:
#
# Создан новый игровой персонаж типа Soldier с атрибутами:\
#     {'name': 'Иван Сусанин', '_Soldier__rank': 'рядовой', '_Soldier__service_number': '12345'}
# Персонаж Иван Сусанин имеет звание рядовой
# Иван Сусанин повышен в звании, он теперь ефрейтор
# Иван Сусанин понижен в звании, он теперь рядовой

def print_info(cls):
    class NewClass(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            print(f"Создан новый игровой персонаж типа {cls.__name__} с атрибутами: {self.__dict__}")

        def get_rank(self):
            print(f"Персонаж {self.name} имеет звание {self._Soldier__rank}")

        def promote(self):
            super().promote()
            print(f"{self.name} повышен в звании, он теперь {self._Soldier__rank}")

        def demote(self):
            super().demote()
            print(f"{self.name} понижен в звании, он теперь {self._Soldier__rank}")

    return NewClass

@print_info
class Soldier:
    def __init__(self, name, rank, service_number):
        self.name = name
        self.__rank = rank
        self.__service_number = service_number

    def verify_service_number(self, service_number):
        return self.__service_number == service_number

    def promote(self):
        if self.__rank in RANKS[:-1]:
            self.__rank = RANKS[RANKS.index(self.__rank) + 1]

    def demote(self):
        if self.__rank in RANKS[1:]:
            self.__rank = RANKS[RANKS.index(self.__rank) - 1]