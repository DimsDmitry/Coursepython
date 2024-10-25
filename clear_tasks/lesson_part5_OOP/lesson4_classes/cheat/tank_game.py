""" Объект - набор свойств и методов, который удобно воспринимать как единое целое
КЛАСС - общее описание того, КАК должны быть устроены объекты одной группы"""
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
        # выстрел - наносит урон противнику
        miss_chance = randint(1, 100)
        if miss_chance > enemy.avoidance:
            # попадание! противнику не повезло
            attack = randint(self.damage - 20, self.damage)
            print(f'ЕСТЬ ПРОБИТИЕ! {self.name} атакует {enemy.name}. Нанесённый урон: {str(attack)}\n')
            enemy.armor -= attack
            if enemy.armor < 0:
                enemy.health += enemy.armor
                enemy.armor = 0
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


sleep(3)

tank1 = Tank('Т-34', 6, 'средний', 'СССР', 20, 100, 50, 60)
tank1.print_info()
sleep(3)

tank2 = Tank('Grill', 10, 'артиллерия', '3-й Рейх', 5, 60, 150, 30)
tank2.print_info()
sleep(3)

tank1.fight(tank2)
