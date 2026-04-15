# Усовершенствуй предыдущую программу. Теперь она должна не печатать скидку, а возвращать результат её работы
# в переменную.


def set_status(score):
    print('Ваша скидка:')
    if 0 < score < 50:
        return 'Скидка 10%'
    elif 50 <= score < 100:
        preturn 'Скидка 15%'
    elif score >= 100:
        return 'Скидка 20%'


score = int(input('Набрано баллов:'))
result = set_status(score)
print(result)
