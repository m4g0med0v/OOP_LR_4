#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Индивидуальное задание №2.
# В следующих заданиях требуется реализовать абстрактный базовый класс,
# определив в нем абстрактные методы и свойства. Эти методы определяются в
# производных классах. В базовых классах должны быть объявлены абстрактные
# методы ввода/вывода, которые реализуются в производных классах.
# Вызывающая программа должна продемонстрировать все варианты вызова
# переопределенных абстрактных методов. Написать функцию вывода, получающую
# параметры базового класса по ссылке и демонстрирующую виртуальный вызов.

# Создать абстрактный базовый класс Function (функция) с виртуальными методами
# вычисления значения функции y=f(x) в заданной точке x и вывода результата на
# экран.Определить производные классы Ellipse (эллипс), Hyperbola (гипербола)
# с собственными функциями вычисления у в зависимости от входного параметра x.
# Уравнение эллипса: (x^2/a^2)+(y^2/b^2)=1; гиперболы: (x^2/a^2)-(y^2/b^2)=1.

import math
from abc import ABC, abstractmethod
from typing import Union


class Function(ABC):
    @abstractmethod
    def calculate_y(self, x: float) -> float:
        """Вычисляет значение функции y=f(x) в точке x."""
        pass

    @abstractmethod
    def display_result(self, x: float) -> None:
        """Выводит результат на экран."""
        pass


class Ellipse(Function):
    def __init__(self, a: float, b: float):
        self.a: float = a
        self.b: float = b

    def calculate_y(self, x: float) -> float:
        """Вычисляет значение y для эллипса в точке x, если возможно."""
        if abs(x) > self.a:
            raise ValueError(
                "Значение x выходит за пределы" "допустимых значений для эллипса"
            )
        y: float = self.b * math.sqrt(1 - (x**2 / self.a**2))
        return y

    def display_result(self, x: float) -> None:
        """Выводит значение y для эллипса при заданном x."""
        y = self.calculate_y(x)
        print(f"Для эллипса с параметрами" f"a={self.a}, b={self.b} и x={x}, y = {y}")


class Hyperbola(Function):
    def __init__(self, a: float, b: float) -> None:
        self.a: float = a
        self.b: float = b

    def calculate_y(self, x: float) -> float:
        """Вычисляет значение y для гиперболы в точке x."""
        y: float = self.b * math.sqrt((x**2 / self.a**2) - 1)
        return y

    def display_result(self, x: float) -> None:
        """Выводит значение y для гиперболы при заданном x."""
        y = self.calculate_y(x)
        print(f"Для гиперболы с параметрами" f"a={self.a}, b={self.b} и x={x}, y = {y}")


# Функция для демонстрации виртуального вызова
def show_function_result(function_obj: Union[Ellipse, Hyperbola], x: float) -> None:
    """Вызывает метод display_result для объекта базового класса Function."""
    function_obj.display_result(x)


if __name__ == "__main__":
    # Создаем объекты для эллипса и гиперболы
    ellipse: Ellipse = Ellipse(a=5, b=3)
    hyperbola: Hyperbola = Hyperbola(a=5, b=3)

    # Демонстрируем вызов методов для эллипса
    print("Вызов для эллипса:")
    show_function_result(ellipse, x=3)
    show_function_result(ellipse, x=6)

    # Демонстрируем вызов методов для гиперболы
    print("\nВызов для гиперболы:")
    show_function_result(hyperbola, x=6)
    show_function_result(hyperbola, x=3)
