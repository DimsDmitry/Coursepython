# Для ПО кондитерской фабрики нужно написать родительский класс Candy (Конфеты).
# Этот класс имеет атрибуты name, price, weight (наименование, цена, вес).
# Подклассы Chocolate, Gummy, HardCandy (шоколад, жевательный мармелад, леденец) наследуют все атрибуты суперкласса Candy.
# Кроме того, у них есть и свои атрибуты:
#
# Chocolate – cocoa_percentage (процент содержания какао) и chocolate_type (сорт шоколада).
# Gummy – flavor и shape (вкус и форма).
# HardCandy – flavor и filled (вкус и начинка).

# Пример:
#
# Шоколадные конфеты:
# Название конфет: Швейцарские луга
# Стоимость: 325.5 руб
# Вес брутто: 220 г
# Процент содержания какао: 40
# Тип шоколада: молочный
#
# Мармелад жевательный:
# Название конфет: Жуй-жуй
# Стоимость: 76.5 руб
# Вес брутто: 50 г
# Вкус: вишня
# Форма: медведь
#
# Фруктовые леденцы:
# Название конфет: Crazy Фрукт
# Стоимость: 35.5 руб
# Вес брутто: 25 г
# Вкус: манго
# Начинка: True

class Candy:
    pass