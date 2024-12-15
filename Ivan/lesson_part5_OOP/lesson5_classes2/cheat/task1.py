"""Допишите программу ниже. Она должна запрашивать характеристики вашего питомца, создавать на их основе объект
класса Animal, и печатать характеристики о нём

Пример:

Какой вид вашего животного?>? кот
Какой оно издаёт звук?>? мяу
Как его зовут?>? Кокос
Чем оно питается?>? влажный и сухой корм
Привет! Я кот по имени Кокос, мяу! Моя еда: влажный и сухой корм
"""


class Animal:
    def __init__(self, species, voice, name, food):
        self.species = species
        self.voice = voice
        self.food = food
        self.name = name

    def print_info(self):
        print(f'Привет! Я {self.species} по имени {self.name}, {self.voice}! Моя еда: {self.food}')


species = input('Какой вид вашего животного?')
voice = input('Какой оно издаёт звук?')
name = input('Как его зовут?')
food = input('Чем оно питается?')

my_animal = Animal(species, voice, name, food)

my_animal.print_info()
