""" Объект - набор свойств и методов, который удобно воспринимать как единое целое
КЛАСС - общее описание того, КАК должны быть устроены объекты одной группы"""
from random import randint
from time import sleep


class Tank:
    """класс, описывающий характеристики танка"""

    def __init__(self, name, lvl, category, nation, armor, health, damage, speed):
        # initialization - запуск. Данный метод называется конструктором класса.
        # отвечает за присваивание свойств объекту класса
        self.name = name  # имя
        self.lvl = lvl  # уровень
        self.category = category  # тип (тяжёлый, средний, лёгкий, артиллерия, ПТ-САУ и т.д.)
        self.nation = nation  # страна (СССР, США, Япония и т.д.)
        self.armor = armor  # броня
        self.health = health  # здоровье
        self.damage = damage  # урон
        self.speed = speed  # скорость
        # свойство класса self.avoidance - будет показывать шанс уклонения в %
        if self.category == 'лёгкий':
            self.avoidance = 50
        elif self.category == 'пт-сау':
            self.avoidance = 35
        elif self.category == 'средний':
            self.avoidance = 30
        elif self.category == 'тяжёлый':
            self.avoidance = 20
        elif self.category == 'артиллерия':
            self.avoidance = 15
        else:
            self.avoidance = 25

    def print_info(self):
        print(f'В битву вступает грозный танк {self.name}')
        print(f'Уровень танка - {self.lvl}, категория - {self.category}')
        print(f'Броня - {self.armor}, здоровье - {self.health}')
        print(f'Мощность орудия - {self.damage}\n')
        sleep(3)

    def shoot(self, enemy):
        """Стреляем в противника, отнимая его очки брони и здоровья"""
        miss_chance = randint(1, 100)
        if miss_chance > enemy.avoidance:
            # попадание! противнику не повезло
            attack = randint(self.damage - 20, self.damage)
            print(f'ЕСТЬ ПРОБИТИЕ! {self.name} атакует {enemy.name}. Нанесённый урон: {attack}')
            sleep(1)
            enemy.armor -= attack
            if enemy.armor < 0:
                # если броня стала ниже нуля - оставшийся урон идёт в здоровье
                enemy.health += enemy.armor
                # а броню обнуляем
                enemy.armor = 0
            print(f'{enemy.name} получил урон! Его броня - {enemy.armor}, здоровье - {enemy.health}\n')
        else:
            print('Промах!\n')
        sleep(4)

    def fight(self, enemy):
        """два танка стреляют друг в друга, пока здоровье одного из них не достигнет 0"""
        while self.health and enemy.health > 0:
            # мы стреляем в противника:
            self.shoot(enemy)
            if enemy.health <= 0:
                print(f'{enemy.name} уничтожен!')
                break
            # противник стреляет в нас:
            enemy.shoot(self)
            if self.health <= 0:
                print(f'{self.name} уничтожен!')
                break


tank1 = Tank('Т-34', 4, 'средний', 'СССР', 50, 200, 50, 60)
tank1.print_info()

tank2 = Tank('Tiger', 7, 'тяжёлый', '3-й Рейх', 80, 250, 80, 20)
tank2.print_info()

tank1.fight(tank2)
