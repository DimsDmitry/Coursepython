"""
Напиши программу, которая будет создавать список из двух элементов:
1) Фамилия ученика (строка)
2) Список его оценок (список)

Пример:

Заполнение профиля ученика
Введите фамилию ученика:>? Олегов
Введите оценки ученика через пробел:>? 5 2 3 5
['Олегов', ['5', '2', '3', '5']]

"""

print('Заполнение профиля ученика')
surname = input('Введите фамилию ученика: ')
grades = input('Введите оценки ученика через пробел: ').split()
profile = [surname, grades]
print(profile)
