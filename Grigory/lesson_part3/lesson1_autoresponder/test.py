def print_label(name, cls):
    print('Имя:', name)
    print('Класс:', cls)
    print('\n')


pupils = int(input('Сколько учеников в группе:'))
for i in range(pupils):
    name = input('Имя ученика:')
    cls = input('Класс ученика:')
    print_label(name, cls)