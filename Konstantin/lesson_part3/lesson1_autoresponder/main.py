from random import *

def recommend_music(genre):
    if genre == 'рэп' or genre == 'реп':
        groups_list = 'Витя АК,Eminem,50 cent,Snoop Dogg'.split(',')
        music = choice(groups_list)
        return music
    if genre == 'рок':
        groups_list = 'Би-2,Linkin Park,Slipknot,Skillet'.split(',')
        music = choice(groups_list)
        return music
print('Здравствуйте! Я - виртуальный помощник Олеся. Я пока немногое умею, но активно учусь')
answer = input('1 - рекомендация музыки, 2 - анекдот, 3 - пообщаться, 4 - магазин. off - завершить')

if answer == '1':
    genre = input('Какой жанр предпочитаете?')
    result = recommend_music(genre)