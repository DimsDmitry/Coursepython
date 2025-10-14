marks = []
sum_marks = 0

mark = int(input('Введите число: (0 - стоп)'))
while mark != 0:
    marks.append(mark)
    sum_marks += mark
    mark = int(input('Введите число: (0 - стоп)'))

average = round(sum_marks/len(marks), 1)
print('Список оценок:', marks)
print('Средний балл:', average)