# допиши программу. Она должна печатать столько бирок на тетради,
# сколько указано учеников в классе
# Пример:
#
# Количество футболок:>? 3
# -ТЕТРАДЬ-
# Ученика 10Б класса по математике
# -ТЕТРАДЬ-
# Ученика 10Б класса по математике
# -ТЕТРАДЬ-
# Ученика 10Б класса по математике




def print_label:
    print('-ТЕТРАДЬ-')
    print('Ученика 10Б класса по математике')

amount = int(input('Количество учеников в 10Б классе:'))
for i in range(amount):
    print_label