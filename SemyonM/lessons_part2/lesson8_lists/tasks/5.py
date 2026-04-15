"""В архиве уже хранится список детей и их оценок. Нужно написать программу, считающую средний балл класса."""

students = ['Иванов - 5', 'Петров - 4', 'Олегова - 3', 'Ромашкина - 4', 'Олюшкин - 5']
summ = 0

"""СПОСОБ 1 - ЧЕРЕЗ split"""

# перебираем элементы списка
for student in students:
    mark = student.split()[2]
    summ += int(mark)

print('Средний балл:', summ/len(students))

"""СПОСОБ 2 - ЧЕРЕЗ СРЕЗЫ"""

# перебираем элементы списка
for student in students:
    mark = student[-1]
    summ += int(mark)

print('Средний балл:', summ/len(students))