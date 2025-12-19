from random import choice


def recommend_music(genre):
    if genre == 'рэп' or genre == 'реп':
        groups_list = 'Витя АК,Eminem,50 cent,Snoop Dogg'.split(',')
        music = choice(groups_list)
        return music
    if genre == 'рок':
        groups_list = 'Би-2,Linkin Park,Slipknot,Skillet'.split(',')
        music = choice(groups_list)
        return music