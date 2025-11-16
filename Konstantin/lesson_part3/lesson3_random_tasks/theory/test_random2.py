from random import shuffle, choice

# 2-й вариант импорта - пишем ТОЛЬКО
# название функции которую мы пишем

# shuffle - функция, которая перемешивает элементы списка
list_nums = [1, 2, 3, 4, 5]
shuffle(list_nums)
print(list_nums)
print(list_nums[0])

# choice - выбирает случайный элемент последовательности
# (списка, строки и тд)
print(choice(list_nums))