from random import shuffle


def check_music():
    genre = input('Введите жанр:')
    if genre.find('реп') != -1 or genre.find('рэп') != -1:
        print('Eminem, 50 cent, Витя АК')
    elif genre.find('рок') != -1:
        print('Король и Шут, Metallica')
    elif genre.find('хип-хоп') != -1:
        print('Weekend, Markul, Rihanna')
    else:
        print('Запрос не распознан. Попробуйте снова')


def tell_joke():
    jokes_list = 'Колобок повесился, Буратино утонул, Русалка села на шпагат'.split(', ')
    shuffle(jokes_list)
    joke = jokes_list[0]
    print(joke)


def talk():
    question = input('Как ваше настроение?')
    if question.find('плохо') != -1:
        print('Не переживайте, всё обязательно наладится!')
    elif question.find('хорошо') != -1 or question.find('отлично') != -1 or question.find('круто') != -1:
        print('Хорошо, когда всё хорошо')
    else:
        print('Не понимаю тебя. Повторите, пожалуйста')


def shop():
    print('Ассортимент нашего фирменного магазина')
    print('Кружка - 400 рублей')
    print('Футболка - 600 рублей')
    print('Блютуз-колонка - 1000 рублей')
