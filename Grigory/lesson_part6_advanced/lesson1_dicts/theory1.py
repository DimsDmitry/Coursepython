"""Словарь - неупорядоченный набор пар ключ-значение.
Изменяемая структура данных"""

# объявить словарь
my_dict = dict()
my_dict = {}
# элементы словаря НЕ ИМЕЮТ ИНДЕКСА
my_dict = {
    'Боевики': 'Рэмбо',
    'Ужасы': 'Оно',
    'Детективы': ['Шерлок Холмс', 'Пёс', 'Преступление и наказание']
}
# КЛЮЧОМ СЛОВАРЯ может быть ТОЛЬКО неизменяемая структура данных:
# число, float, строка, bool, кортежи, замороженные множества

# ЗНАЧЕНИЕМ СЛОВАРЯ может быть ЛЮБАЯ структура данных:
# число, float, строка, bool, список, словарь, кортежи, множества, замороженные множества

# обращение к элементу словаря:
print(my_dict['Боевики'])
# получить 'Преступление и наказание':
print(my_dict['Детективы'][2])
# вывести все значения словаря:
print(my_dict.values())
# вывести все ключи словаря:
print(my_dict.keys())
# вывести все пары К-З словаря:
print(my_dict.items())

# словарь - изменяемая структура данных!
# добавить в словарь пару "ключ-значение"
my_dict['Комедии'] = 'Кухня'
print(my_dict)
# удалить пару "ключ-значение"
del my_dict['Ужасы']
print(my_dict)
# перезаписать "ключ-значение"
my_dict['Боевики'] = 'Терминатор'
# ключи в словаре уникальны, значения - нет
print(my_dict)

# вывести все ключи словаря:
for elem in my_dict:
    print(elem)
print('\n')

# вывести все значения словаря:
for elem in my_dict:
    print(my_dict[elem])

user = {
    login: 'dimasik',
    password: '123',
    county: 'Russia',
    is_confirm: True
}
