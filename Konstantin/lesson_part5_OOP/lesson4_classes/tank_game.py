""" Объект - набор свойств и методов, который удобно воспринимать как единое целое
КЛАСС - общее описание того, КАК должны быть устроены объекты одной группы"""

"""свойства класса танк:
название, уровень (1-10), категория (средний, тяжелый и тд), страна, броня, здоровье, урон, скорость

Также уже будут: шанс уклонения (зависит от категории)

Методы:
- print_info
- shoot - выстрел по врагу, с шансом равным шансу уклонения противника будет промах
Если попали - снимаем очки сначала с брони, потом со здоровья
- fight - два танка стреляют друг в друга, пока один из них не погибнет (здоровье == 0)

"""
from random import randint
from time import sleep


class Tank:
    """класс, описывающий характеристики танка"""

    def __init__(self, name, lvl, category, nation, armor, health, damage, speed):
        # initialization - инициализация/запуск/включение
        self.name = name  # название танка
        self.lvl = lvl  # уровень танка
        self.category = category  # тип танка (тяжелый, легкий, средний, артиллерия и т.д.)
        self.nation = nation  # страна, к которой принадлежит танк
        self.armor = armor  # броня танка
        self.health = health  # здоровье танка
        self.damage = damage  # урон, который наносит танк
        self.speed = speed  # скорость передвижения танка, км/ч
        # шанс уклонения в %
        if self.category == 'лёгкий':
            self.avoidance = 50
        if self.category == 'пт-сау':
            self.avoidance = 35
        if self.category == 'средний':
            self.avoidance = 30
        if self.category == 'тяжёлый':
            self.avoidance = 20
        if self.category == 'артиллерия':
            self.avoidance = 15
        else:
            self.avoidance = 35

    def print_info(self):
        print(f'В битву вступает грозный танк {self.name}')
        print(f'Уровень танка - {self.lvl}, категория - {self.category}')
        print(f'Броня - {self.armor}, здоровье - {self.health}')
        print(f'Мощность орудия - {self.damage}')
        print(f'Шанс уклонения - {self.avoidance}\n')

    def shoot(self, enemy):
        """выстрел - наносим урон противнику"""
        miss_chance = randint(1, 100)
        if miss_chance > enemy.avoidance:
            # попадание!
            attack = randint(int(self.damage * 0.8), self.damage)
            print(f'ЕСТЬ ПРОБИТИЕ! {self.name} атакует {enemy.name}')
            print(f'Нанесённый урон - {attack}\n')
            enemy.armor -= attack
            # проверяем, осталась ли броня. если нет, то оставшийся урон уходит в очки здоровья
            if enemy.armor < 0:
                enemy.health += enemy.armor
                enemy.armor = 0
            # пишем, сколько осталось брони и здоровья у противника
            print(f'{enemy.name} получил урон! Его броня - {enemy.armor}, здоровье - {enemy.health}\n')
        else:
            print('Промах!\n')

    def fight(self, enemy):
        """битва длится, пока здоровье одного из танков не достигнет 0"""
        while self.health and enemy.health > 0:
            self.shoot(enemy)
            if enemy.health <= 0:
                print(enemy.name, 'уничтожен!')
                break
            sleep(10)

            enemy.shoot(self)
            if self.health <= 0:
                print(self.name, 'уничтожен!')
                break
            sleep(10)
