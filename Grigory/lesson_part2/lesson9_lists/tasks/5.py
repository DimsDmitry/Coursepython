"""В архиве уже хранится список детей и их оценок. Нужно написать программу, считающую средний балл класса."""

students = ['Иванов - 5', 'Петров - 4', 'Олегова - 3', 'Ромашкина - 4', 'Олюшкин - 5']

'''Вариант 1'''
# summ = 0
# for st in students:
#     summ += int(st.split()[2])
#
# result = summ/len(students)
# print('Средний балл:', result)


'''Вариант 2'''
summ = 0
for st in students:
    summ += int(st[-1])

result = summ/len(students)
print('Средний балл:', result)