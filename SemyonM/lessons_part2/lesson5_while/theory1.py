password_true = '12345'
password = input('Введите пароль: ')

while password != password_true:
    print('Пароль неверный!')
    password = input('Введите пароль: ')

print('Пароль принят.')