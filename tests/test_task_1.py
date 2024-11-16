import unittest

from src.task_1 import Hero, Soldier


class TestGame(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print(f"{cls.__name__:=^80}")

    @classmethod
    def tearDownClass(cls) -> None:
        print("=" * 80)

    # Проверяет, что уровень героя увеличивается.
    def test_hero_increase_level(self) -> None:
        hero = Hero(team=1)
        initial_level = hero.level
        hero.increase_level()
        self.assertEqual(hero.level, initial_level + 1)

    # Проверяет, что солдат не может следовать за героем другой команды
    def test_soldier_follow_hero_wrong_team(self) -> None:
        hero = Hero(team=1)
        soldier = Soldier(team=2)
        with self.assertRaises(ValueError):
            soldier.follow_hero(hero)

    # Проверяет, что количество солдат в каждой
    # команде соответствует ожиданиям.
    def test_soldiers_count(self) -> None:
        soldiers_team_1 = [Soldier(team=1) for _ in range(10)]
        soldiers_team_2 = [Soldier(team=2) for _ in range(5)]
        self.assertEqual(len(soldiers_team_1), 10)
        self.assertEqual(len(soldiers_team_2), 5)
