import pytest
from src.task_1 import Hero, Soldier


class TestGame:
    def test_hero_increase_level(self):
        hero = Hero(team=1)
        initial_level = hero.level
        hero.increase_level()
        assert hero.level == initial_level + 1

    def test_soldier_follow_hero_wrong_team(self):
        hero = Hero(team=1)
        soldier = Soldier(team=2)
        with pytest.raises(ValueError):
            soldier.follow_hero(hero)

    def test_soldiers_count(self):
        soldiers_team_1 = [Soldier(team=1) for _ in range(10)]
        soldiers_team_2 = [Soldier(team=2) for _ in range(5)]
        assert len(soldiers_team_1) == 10
        assert len(soldiers_team_2) == 5
