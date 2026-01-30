login = input('Придумайте логин!')
wrong = '!@#$%^&*()_=+/'
for s in login:
    if s in wrong:
        print('Обнаружен запрещённый символ:', s)