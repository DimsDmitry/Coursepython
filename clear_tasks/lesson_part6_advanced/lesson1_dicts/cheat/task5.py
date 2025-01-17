author = input('Испытайте удачу! Введите автора:')
if author in authors:
    number = randint(0, 2)
    print('Рекомендованная книга:', authors[author][number])
else:
    print('Автор не найден!')
