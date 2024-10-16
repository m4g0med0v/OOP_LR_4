#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Индивидуальное задание №2. В следующих заданиях требуется реализовать
# абстрактный базовый класс, определив в нем абстрактные методы и свойства.
# Эти методы определяются в производных классах. В базовых классах должны быть
# объявлены абстрактные методы ввода/вывода, которые реализуются в производных
# классах. Вызывающая программа должна продемонстрировать все варианты вызова
# переопределенных абстрактных методов. Написать функцию вывода, получающую
# параметры базового класса по ссылке и демонстрирующую виртуальный вызов.

# Создать абстрактный базовый класс Function (функция) с виртуальными методами
# вычисления значения функции y=f(x) в заданной точке x и вывода результата на
# экран.Определить производные классы Ellipse (эллипс), Hyperbola (гипербола) с
# собственными функциями вычисления у в зависимости от входного параметра x.
# Уравнение эллипса: (x**2a**2)+(y**2b**2)=1;
# гиперболы: (x**2a**2)-(y**2b**2)=1.


from abc import ABC, abstractmethod
import math


class Function(ABC):
    @abstractmethod
    def calculate_y(self, x):
        """Вычисляет значение функции y=f(x) в заданной точке x."""
        pass

    @abstractmethod
    def display(self, x):
        """Выводит результат вычисления функции в точке x."""
        pass


class Ellipse(Function):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_y(self, x):
        """Вычисляет значение y для эллипса."""
        if abs(x) > self.a:
            raise ValueError("Для данного x нет действительного значения y")
        y = self.b * math.sqrt(1 - (x**2) / (self.a**2))
        return y

    def display(self, x):
        try:
            y = self.calculate_y(x)
            print(f"Ellipse: x = {x}, y = ±{y}")
        except ValueError as e:
            print(f"Ellipse: {e}")


class Hyperbola(Function):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_y(self, x):
        """Вычисляет значение y для гиперболы."""
        if abs(x) < self.a:
            raise ValueError("Для данного x нет действительного значения y")
        y = self.b * math.sqrt((x**2) / (self.a**2) - 1)
        return y

    def display(self, x):
        try:
            y = self.calculate_y(x)
            print(f"Hyperbola: x = {x}, y = ±{y}")
        except ValueError as e:
            print(f"Hyperbola: {e}")


def show_function_value(func: Function, x):
    """Выводит значение функции, используя абстрактный базовый класс Function."""
    func.display(x)


if __name__ == "__main__":
    # Создаем экземпляры эллипса и гиперболы
    ellipse = Ellipse(a=5, b=3)
    hyperbola = Hyperbola(a=5, b=3)

    # Демонстрация работы с эллипсом
    print("Demonstrating Ellipse:")
    show_function_value(ellipse, 3)
    show_function_value(ellipse, 5)  # На границе определения
    show_function_value(ellipse, 6)  # За пределами области определения

    print("\nDemonstrating Hyperbola:")
    # Демонстрация работы с гиперболой
    show_function_value(hyperbola, 6)
    show_function_value(hyperbola, 5)  # На границе определения
    show_function_value(hyperbola, 4)  # За пределами области определения
