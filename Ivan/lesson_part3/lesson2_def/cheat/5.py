# Напиши функцию set_status. Она должна принимать количество набранных баллов на экзамене, анализировать его и печатать
# сообщение «Ваша скидка:» и скидку:

# — от 0 до 49 баллов — «Скидка 10%»;
# — от 50 до 99 баллов — «Скидка 15%»;
# — от 100 баллов и выше — «Скидка 20%».
# Пример:
#
# Набрано баллов:>? 67
# Ваша скидка:
# Скидка 15%


def set_status(score):
    print('Ваша скидка:')
    if 0 < score < 50:
        print('Скидка 10%')
    elif 50 <= score < 100:
        print('Скидка 15%')
    elif score >= 100:
        print('Скидка 20%')


score = int(input('Набрано баллов:'))
set_status(score)