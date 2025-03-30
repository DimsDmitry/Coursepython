# Проверка списка
#
# Описание: Напишите функцию check_list(lst), которая принимает список. Если список пустой, функция должна вызывать
# исключение IndexError с сообщением "Список не может быть пустым".
# Если в списке есть элементы, которые не являются числами, функция должна вызывать исключение TypeError
# с сообщением "Все элементы списка должны быть числами".
# В противном случае функция должна возвращать сумму всех чисел в списке.

def check_list(lst):
    # Проверка на пустой список
    if not lst:
        raise IndexError("Список не может быть пустым")

    # Проверка на наличие нечисловых элементов
    for item in lst:
        if not isinstance(item, (int, float)):
            raise TypeError("Все элементы списка должны быть числами")

    # Возврат суммы всех чисел в списке
    return sum(lst)


# Примеры использования функции
try:
    print(check_list([]))  # Это вызовет IndexError
except Exception as e:
    print(e)

try:
    print(check_list([1, 2, 'a', 4]))  # Это вызовет TypeError
except Exception as e:
    print(e)

try:
    print(check_list([1, 2, 3.5, 4]))  # Это вернет 10.5
except Exception as e:
    print(e)