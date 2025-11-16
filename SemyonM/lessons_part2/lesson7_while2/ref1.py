password = input('Введите пароль:')
attempts = 1
while password != 'abc529_123':
    attempts += 1
    print('Ошибка!')
    password = input('Введите пароль:')
print('Промокод засчитан с', attempts, 'попытки')
