from random import *

from music import recommend_music
from joke import get_joke



print('Здравствуйте! Я - виртуальный помощник Олеся. Я пока немногое умею, но активно учусь')
answer = input('1 - рекомендация музыки, 2 - анекдот, 3 - пообщаться, 4 - магазин. off - завершить')

if answer == '1':
    genre = input('Какой жанр предпочитаете?')
    result = recommend_music(genre)
    print(result)
if answer == '2':
    print(get_joke())