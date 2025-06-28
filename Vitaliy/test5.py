password = '123'
answer = input('Пароль!')

i = 1

while answer != password and i < 3:
    print('Доступ запрещён!')
    answer = input('Пароль!')
    i += 1

