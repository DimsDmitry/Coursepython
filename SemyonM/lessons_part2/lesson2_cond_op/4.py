mark1 = int(input('Введите баллы по математике:'))
mark2 = int(input('Введите баллы по русскому:'))
average = (mark1 + mark2) / 2
print('Средний балл:', average)
if average > 30:
    print('Вы прошли порог')
if average > 50:
    print('Поздравляем! Вы прошли вступительный конкурс')
else:
    print('К сожалению, вступительный конкурс вы не прошли')

