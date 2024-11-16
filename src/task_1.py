#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Разработайте программу по следующему описанию.В некой игре-стратегии есть
# солдаты и герои. У всех есть свойство, содержащее уникальный номер объекта,
# и свойство, в котором хранится принадлежность команде. У солдат есть метод
# "иду за героем", который в качестве аргумента принимает объект типа "герой".
# У героев есть метод увеличения собственного уровня. В основной ветке
# программы создается по одному герою для каждой команды. В цикле генерируются
# объекты-солдаты. Их принадлежность команде определяется случайно. Солдаты
# разных команд добавляются в разные списки. Измеряется длина списков солдат
# противоборствующих команд и выводится на экран. У героя, принадлежащего
# команде с более длинным списком, увеличивается уровень. Отправьте одного из
# солдат первого героя следовать за ним. Выведите на экран идентификационные
# номера этих двух юнитов.


import random


class Unit:
    _id_counter: int = 1

    def __init__(self, team: int) -> None:
        self.id: int = Unit._id_counter
        Unit._id_counter += 1
        self.team: int = team


class Hero(Unit):
    def __init__(self, team: int) -> None:
        super().__init__(team)
        self.level: int = 1

    def increase_level(self) -> None:
        self.level += 1
        print(f"Герой {self.id} повысил уровень до {self.level}")


class Soldier(Unit):
    def follow_hero(self, hero: Hero) -> None:
        if isinstance(hero, Hero) and hero.team == self.team:
            print(f"Солдат {self.id} следует за героем {hero.id}")
        else:
            raise ValueError(f"Солдат {self.id} не может следовать за героем {hero.id}")


if __name__ == "__main__":
    # Создаем героев для двух команд
    hero_team_1 = Hero(team=1)
    hero_team_2 = Hero(team=2)

    # Создаем списки солдат для каждой команды
    soldiers_team_1 = []
    soldiers_team_2 = []

    # Генерируем солдат и распределяем их по командам
    for _ in range(100):
        team = random.choice([1, 2])
        soldier = Soldier(team=team)
        if team == 1:
            soldiers_team_1.append(soldier)
        else:
            soldiers_team_2.append(soldier)

    # Выводим количество солдат в каждой команде
    print(f"Солдаты команды 1: {len(soldiers_team_1)}")
    print(f"Солдаты команды 2: {len(soldiers_team_2)}")

    # Определяем команду с большим числом солдат и
    # повышаем уровень героя этой команды
    if len(soldiers_team_1) > len(soldiers_team_2):
        hero_team_1.increase_level()
    else:
        hero_team_2.increase_level()

    # Отправляем одного из солдат команды первого героя следовать за ним
    if soldiers_team_1:
        soldiers_team_1[0].follow_hero(hero_team_1)

    # Выводим идентификационные номера героя и солдата
    print(f"Герой: {hero_team_1.id}, Солдат: {soldiers_team_1[0].id}")
