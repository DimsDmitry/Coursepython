marks = [2, 3, 3, 4, 4, 5, 5, 2, 3]
amount = len(marks)  # кол-во оценок равно длине списка
summ = 0

for mark in marks:
    summ += mark
    print(summ)

print('Среднее:', summ/amount)