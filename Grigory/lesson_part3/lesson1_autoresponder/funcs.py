def music():
    # запрашивает у пользователя жанр и предлагает исполнителя
    genre = input('Какой жанр музыки вы предпочитаете?').lower()
    if genre.find('рэп') != -1 or genre.find('реп') != -1:
        return 'АК-47, Eminem, Баста'
    elif genre.find('рок') != -1:
        return 'Linkin park, Metallica, Сектор Газа, Би-2'
    elif genre.find('хип') != -1:
        return 'Джастин Бибер, Rihanna, Markul'
    return 'Мы не поняли ваш запрос. Послушайте инстасамку'


def get_joke():
    pass


def talking():
    """пообщаться с пользователем"""
    pass
