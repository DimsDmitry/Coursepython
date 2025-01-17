# В программе хранится информация о самых популярных книгах библиотеки. В предпочтениях читателей произошли изменения.
#
# Внеси изменения в цифровой каталог:
# 1. Добавь в books новые популярные книги:
# - Дефо: Приключения Робинзона Крузо,
# - Дюма: Граф Монте-Кристо.
#
# 2. Удалить книгу:
# - Пушкин: Капитанская дочка.
#
# Запусти программу и убедись, что база и предпочтения обновлены

books = {
    'Пушкин': 'Капитанская дочка',
    'Лондон': 'Белый клык',
    'Кэрролл': 'Алиса в стране чудес',
    'Линдгрен': 'Карлсон, который живёт на крыше'
}

# добавь два наименования
# удали одно наименование

if 'Дефо' in books and 'Дюма' in books:
    print('База обновлена!')
if not ('Пушкин' in books):
    print('Предпочтения обновлены')
