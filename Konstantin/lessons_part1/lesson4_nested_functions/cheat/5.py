# # Создайте программу, которая запрашивает у пользователя две строки и выводит,
# # какая из них длиннее, или если они равны по длине.
# ВАЖНО - программа должна состоять из одной строки. Сделайте вывод - адекватно ли выглядит такое сокращение кода?
#
# Пример:
#
# Первая строка:>? Первая строка
# Вторая строка:>? А это вторая!!!
# False


print(len(input('Первая строка:')) > len(input('Вторая строка:')))
