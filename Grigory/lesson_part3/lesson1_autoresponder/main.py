from funcs import *


print('Здравствуйте! Я - виртуальный помощник Пётр. Я пока немногое умею, но активно учусь')
answer = input('1 - рекомендация музыки, 2 - анекдот, 3 - пообщаться, 4 - магазин. off - завершить')
while answer != 'off':
    if answer == '1':
        result = music()
        print(result)
        answer = input('1 - рекомендация музыки, 2 - анекдот, 3 - пообщаться, 4 - магазин. off - завершить')
    if answer == '2':
        result = get_joke()
        print(result)
    if answer == '3':
        result = talking()
        print(result)