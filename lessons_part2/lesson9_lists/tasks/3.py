"""Напиши программу, запрашивающую ввод  игры, пока не введён 0 (сигнал конца ввода).
1. Если такая игра уже есть в списке, то должно печататься: «Эта игра уже записана».
2. Если такой игры ещё нет, то игра добавляется в список. Список сортируется по алфавиту.

Пример:

Введи игру (0 - остановить ввод):>? cs go
Введи игру (0 - остановить ввод):>? dota
Введи игру (0 - остановить ввод):>? dota
Эта игра уже записана
Введи игру (0 - остановить ввод):>? 0
Список игр: ['cs go', 'dota']
"""

games = []
game = ('Введи игру (0 - остановить ввод):')
game = game.lower()
while game != '0':

print('Список игр:'
games)