#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Индивидуальное задание №1.
# Составить программу с использованием иерархии классов. Номер варианта
# необходимо получить у преподавателя. В раздел программы, начинающийся после
# инструкции if __name__ = '__main__': добавить код, демонстрирующий
# возможности разработанных классов.
#
# Создать класс Triangle с полями-сторонами. Определить методы изменения
# сторон, вычисления углов, вычисления периметра. Создать производный класс
# RightAngled (прямоугольный), имеющий поле площади. Определить метод
# вычисления площади.

import math
from typing import Tuple


class Triangle:
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c
        if not self._is_valid_triangle():
            raise ValueError("Стороны не образуют треугольник")

    def set_sides(self, a: float, b: float, c: float) -> None:
        """Изменяет длины сторон треугольника."""
        self.a = a
        self.b = b
        self.c = c
        if not self._is_valid_triangle():
            raise ValueError("Стороны не образуют треугольник")

    def _is_valid_triangle(self) -> bool:
        """Проверяет, образуют ли заданные стороны треугольник."""
        return (
            (self.a + self.b > self.c)
            and (self.a + self.c > self.b)
            and (self.b + self.c > self.a)
        )

    def perimeter(self) -> float:
        """Вычисляет периметр треугольника."""
        return self.a + self.b + self.c

    def angles(self) -> Tuple[float, float, float]:
        """Вычисляет углы треугольника в градусах."""
        angle_A = math.degrees(
            math.acos((self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c))
        )
        angle_B = math.degrees(
            math.acos((self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c))
        )
        angle_C = 180 - angle_A - angle_B
        return angle_A, angle_B, angle_C


class RightAngled(Triangle):
    def __init__(self, a: float, b: float) -> None:
        """
        Инициализирует прямоугольный треугольник с катетами a и b,
        вычисляет гипотенузу.
        """
        c = math.sqrt(a**2 + b**2)
        super().__init__(a, b, c)
        self.area = self.calculate_area()

    def calculate_area(self) -> float:
        """Вычисляет площадь прямоугольного треугольника."""
        return 0.5 * self.a * self.b


if __name__ == "__main__":
    # Создаем обычный треугольник
    triangle = Triangle(3, 4, 5)
    print("Периметр треугольника:", triangle.perimeter())
    print("Углы треугольника:", triangle.angles())

    # Создаем прямоугольный треугольник
    right_triangle = RightAngled(3, 4)
    print("Периметр прямоугольного треугольника:", right_triangle.perimeter())
    print("Площадь прямоугольного треугольника:", right_triangle.area)
    print("Углы прямоугольного треугольника:", right_triangle.angles())
