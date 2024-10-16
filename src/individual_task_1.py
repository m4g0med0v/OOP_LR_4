#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Индивидуальное задание №1. Составить программу с использованием иерархии
# классов. Номер варианта необходимо получить у преподавателя. В раздел
# программы, начинающийся после инструкции if __name__ = '__main__':
# добавить код, демонстрирующий возможности разработанных классов.

# Создать класс Triangle с полями-сторонами. Определить методы изменения сторон,
# вычисления углов, вычисления периметра. Создать производный класс RightAngled
# (прямоугольный), имеющий поле площади. Определить метод вычисления площади.

import math


class Triangle:
    def __init__(self, a, b, c):
        self.set_sides(a, b, c)

    def set_sides(self, a, b, c):
        """Устанавливает длины сторон треугольника и проверяет их корректность."""
        if a + b > c and a + c > b and b + c > a:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError("Стороны не образуют треугольник")

    def perimeter(self):
        """Вычисляет периметр треугольника."""
        return self.a + self.b + self.c

    def angles(self):
        """Вычисляет углы треугольника в градусах."""
        angle_a = math.degrees(
            math.acos((self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c))
        )
        angle_b = math.degrees(
            math.acos((self.a**2 + self.c**2 - self.b**2) / (2 * self.a * self.c))
        )
        angle_c = 180 - angle_a - angle_b
        return angle_a, angle_b, angle_c

    def __str__(self):
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"


class RightAngled(Triangle):
    def __init__(self, a, b):
        """Инициализирует прямоугольный треугольник по катетам a и b."""
        # Гипотенуза вычисляется по теореме Пифагора.
        c = math.sqrt(a**2 + b**2)
        super().__init__(a, b, c)

    def area(self):
        """Вычисляет площадь прямоугольного треугольника."""
        return 0.5 * self.a * self.b

    def __str__(self):
        return f"RightAngled(a={self.a}, b={self.b}, c={self.c}, area={self.area()})"


if __name__ == "__main__":
    # Создаем обычный треугольник
    triangle = Triangle(3, 4, 5)
    print(triangle)
    print(f"Периметр треугольника: {triangle.perimeter()}")
    angles = triangle.angles()
    print(f"Углы треугольника: A={angles[0]:.2f}, B={angles[1]:.2f}, C={angles[2]:.2f}")

    # Создаем прямоугольный треугольник
    right_triangle = RightAngled(3, 4)
    print(right_triangle)
    print(f"Периметр прямоугольного треугольника: {right_triangle.perimeter()}")
    print(f"Площадь прямоугольного треугольника: {right_triangle.area()}")
    angles = right_triangle.angles()
    print(
        f"Углы прямоугольного треугольника: A={angles[0]:.2f}, B={angles[1]:.2f}, C={angles[2]:.2f}"
    )
