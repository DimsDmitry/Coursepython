from random import choice


def get_joke():
    joke_list = []
    joke_list.append('Буратино утонул')
    joke_list.append('Колобок повесился')
    joke_list.append('Анекдот №3')
    joke_list.append('Анекдот №4')
    joke_list.append('Анекдот №5')
    random_joke = choice(joke_list)
    return random_joke
