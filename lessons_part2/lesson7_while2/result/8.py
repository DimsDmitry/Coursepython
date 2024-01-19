# Программа должна запрашивать ввод промокода до тех пор, пока не будет введён промокод «kitty» или пока не закончатся
# 3 попытки ввода.
#
# 1. Если введён неверный промокод, программа должна запросить ввод снова. Всего — 3 попытки.
# 2. Если введён верный промокод, программа печатает: «Принято с попытки _» и завершает работу.
# 3. Если попытки исчерпаны, то программа завершает работу
#
# Пример:
#
# Введите промокод:>? hello
# Введите промокод:>? kitty
# Принято с попытки № 2

attempts = 0
promo = ''
while attempts < 3 and promo != 'kitty':
    promo = input('Введите промокод:')
    attempts += 1
if promo == 'kitty':
    print('Принято с попытки №', attempts)
