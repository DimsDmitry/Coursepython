"""Программа помогает приложению учитывать музыкальные вкусы пользователей.
Она запрашивает ввод названия жанра:

1. Если пользователь вносил такое пожелание, то печатается: «Запрос найден в пожеланиях».
2. Если такое пожелание не вносилось, то печатается: «Такого пожелания нет».
"""

music = ['хип-хоп', 'рок', 'рэп']
searching = input('Запрос:')
searching = searching.lower()