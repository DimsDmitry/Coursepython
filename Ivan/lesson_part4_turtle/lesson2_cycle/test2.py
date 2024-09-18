amount_students = int(input('Сколько учеников в классе?'))
list_students = []

for i in range(amount_students):
    name = input('Имя студента:')
    list_students.append(name)

for s in list_students:
    print(s)
