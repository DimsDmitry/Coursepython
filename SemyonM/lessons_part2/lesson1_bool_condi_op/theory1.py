# Создание логических типов данных. Способ 1:

# res1 = True
# res2 = False

# Способ 2 - логическое выражение:

# операторы >, >=, <, <=, !=, ==

# """ПРОСТЫЕ логические выражения"""
res = 5 > 2
print(res)
print(type(res))

res = (5 != 2)
print(res)

password = 'qwerty'
password_new = input('Введите пароль:')
print('Открыть доступ:', password == password_new)

# """СОСТАВНЫЕ логические выражения - проверка двух и более условий"""
sweets = int(input('Сколько КГ конфет на складе?'))
container = sweets < 50 or sweets > 300

# or - выполнение ХОТЯ БЫ ОДНОГО условия
print('Ошибка хранения конфет:', container)

mathem = int(input('Баллы по математике:'))
rus_lang = int(input('Баллы по русскому языку'))

result = mathem > 90 and rus_lang > 80

# AND - выполнение ВСЕХ условий
print('Успешное поступление в ВУЗ:', result)