from funcs import *


print('Здравствуйте! Я - виртуальный помощник Олеся. Я пока немногое умею, но активно учусь')
answer = input('1 - рекомендация музыки, 2 - анекдот, 3 - пообщаться, 4 - магазин. off - завершить')
while answer != 'off':
    if answer == '1':
        check_music()
        answer = input('1 - рекомендация музыки, 2 - анекдот, 3 - пообщаться, 4 - магазин. off - завершить')
    if answer == '2':
        tell_joke()
        answer = input('1 - рекомендация музыки, 2 - анекдот, 3 - пообщаться, 4 - магазин. off - завершить')
    if answer == '3':
        talk()
        answer = input('1 - рекомендация музыки, 2 - анекдот, 3 - пообщаться, 4 - магазин. off - завершить')
    if answer == '4':
        shop()
        answer = input('1 - рекомендация музыки, 2 - анекдот, 3 - пообщаться, 4 - магазин. off - завершить')

print('Работа завершена. Хорошего дня!')