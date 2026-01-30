# Запросите у пользователя пароль,
# и в случае введения правильного пароля предоставьте ему доступ в личный кабинет

print('Здравствуйте, user528!')
password = input('Введите пароль:')
right = 'qwerty129'
while password != right:
    print('Пароль неправильный! попробуйте ещё раз')
    password = input('Введите пароль:')
print('Доступ в личный кабинет открыт!')


# ВАРИАНТ 1
while password != right:
    print('Пароль неправильный! попробуйте ещё раз')
    password = input('Введите пароль:')

# ВАРИАНТ 2
while input('Введите пароль:') != right:
    print('Пароль неправильный! попробуйте ещё раз')

# ВАРИАНТ 3

while True:
    print('Пароль неверный!')
    password = input('Введите пароль: ')
    if password == password_true:
        break