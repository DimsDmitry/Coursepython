# Написать программу, оповещающую об ошибке хранения овощей на складе.
# Ошибка хранения возникает, когда хранилище почти опустело (меньше 100 кг) или когда оно переполнено (больше 500 кг).
weight = int(input('Введите количество овощей на складе: '))
error = (weight < 100) or (weight > 500)
print('Ошибка хранения:', error)
