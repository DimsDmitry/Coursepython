# Напишите функцию contains, которая принимает кортеж и элемент, и возвращает True,
# если элемент присутствует в кортеже, иначе — False.

def contains(t, element):
    return element in t


my_tuple = (1, 2, 3, 4)
print(contains(my_tuple, 3))  # True
print(contains(my_tuple, 5))  # False
