"""
Напиши программу, которая будет создавать список из двух элементов:
1) Фамилия ученика (строка)
2) Список его оценок (список)

Пример:

Заполнение профиля ученика
Введите фамилию ученика:>? Олегов
Введите оценки ученика:>? 5 2 3 5
['Олегов', ['5', '2', '3', '5']]

"""

print('Заполнение профиля ученика')
student_name = input('Введите фамилию ученика:')
student_marks = input('Введите оценки ученика:')
student_marks = student_marks.split(' ')
student = list()
student.append(student_name)
student.append(student_marks)
print(student)