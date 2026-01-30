marks = input('Введите оценки через пробел').split()
print('Список оценок:', marks)
for mark in marks:
    if mark == '2':
        print('Обнаружена двойка!')
