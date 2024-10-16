#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Разработайте программу по следующему описанию. В некой игре-стратегии есть
# солдаты и герои. У всех есть свойство, содержащее уникальный номер объекта,
# и свойство, в котором хранится принадлежность команде. У солдат есть метод
# "иду за героем", который в качестве аргумента принимает объект типа "герой".
# У героев есть метод увеличения собственного уровня. В основной ветке программы
# создается по одному герою для каждой команды. В цикле генерируются
# объекты-солдаты. Их принадлежность команде определяется случайно.
# Солдаты разных команд добавляются в разные списки. Измеряется длина списков
# солдат противоборствующих команд и выводится на экран. У героя, принадлежащего
# команде с более длинным списком, увеличивается уровень. Отправьте одного из
# солдат первого героя следовать за ним. Выведите на экран идентификационные
# номера этих двух юнитов.

import random


class Unit:
    _id_counter = 1

    def __init__(self, team):
        self.id = Unit._id_counter
        Unit._id_counter += 1
        self.team = team


class Hero(Unit):
    def __init__(self, team):
        super().__init__(team)
        self.level = 1

    def level_up(self):
        self.level += 1
        print(f"Hero {self.id} from team {self.team} leveled up to {self.level}")


class Soldier(Unit):
    def __init__(self, team):
        super().__init__(team)

    def follow_hero(self, hero):
        print(f"Soldier {self.id} follows Hero {hero.id}")


if __name__ == "__main__":
    # Создаем героев для двух команд
    hero1 = Hero("Team A")
    hero2 = Hero("Team B")

    # Списки для хранения солдат каждой команды
    soldiers_team_a = []
    soldiers_team_b = []

    # Генерируем солдат и распределяем их по командам случайным образом
    for _ in range(20):
        team = random.choice(["Team A", "Team B"])
        soldier = Soldier(team)
        if team == "Team A":
            soldiers_team_a.append(soldier)
        else:
            soldiers_team_b.append(soldier)

    # Определяем более многочисленную команду
    if len(soldiers_team_a) > len(soldiers_team_b):
        hero1.level_up()
    else:
        hero2.level_up()

    # Отправляем одного из солдат первой команды следовать за героем
    if soldiers_team_a:
        soldiers_team_a[0].follow_hero(hero1)

    # Выводим идентификационные номера героя и солдата
    if soldiers_team_a:
        print(f"Hero ID: {hero1.id}, Soldier ID: {soldiers_team_a[0].id}")
