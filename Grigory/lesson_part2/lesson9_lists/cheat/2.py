music = ['хип-хоп', 'рок', 'рэп']
searching = input('Запрос:')
searching = searching.lower()
if searching in music:
    print('Запрос найден в пожеланиях')
else:
    print('Такого пожелания нет')