import unittest
from math import isclose

from src.individual_task_2 import Ellipse, Hyperbola, show_function_result


class TestFunction(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print(f"{cls.__name__:=^80}")

    @classmethod
    def tearDownClass(cls) -> None:
        print("=" * 80)

    # Тест на вычисление y для эллипса
    def test_ellipse_calculate_y(self) -> None:
        ellipse = Ellipse(a=5, b=3)

        # Для x = 3, y должно быть положительным
        y = ellipse.calculate_y(3)
        self.assertTrue(isclose(y, 2.4, rel_tol=1e-2))

        # Для x = 0, y должно быть b
        y = ellipse.calculate_y(0)
        self.assertEqual(y, 3)

        # Для x = 6, должно возникнуть исключение
        with self.assertRaises(ValueError):
            ellipse.calculate_y(6)

    # Тест на вычисление y для гиперболы
    def test_hyperbola_calculate_y(self) -> None:
        hyperbola = Hyperbola(a=5, b=3)

        # Для x = 6, y должно быть положительным
        y = hyperbola.calculate_y(6)
        self.assertTrue(isclose(y, 1.98, rel_tol=1e-2))

        # Для x = 3, должно возникнуть исключение
        with self.assertRaises(ValueError):
            hyperbola.calculate_y(3)

    # Тест на вывод для эллипса
    def test_display_result_ellipse(self) -> None:
        ellipse = Ellipse(a=5, b=3)

        # Перехватываем вывод
        with self.assertRaises(ValueError):
            ellipse.display_result(6)

        # Для x = 3, проверим корректный вывод
        ellipse.display_result(2)

    # Тест на вывод для гиперболы
    def test_display_result_hyperbola(self) -> None:
        hyperbola = Hyperbola(a=5, b=3)

        # Перехватываем вывод
        with self.assertRaises(ValueError):
            hyperbola.display_result(3)

        # Для x = 6, проверим корректный вывод
        hyperbola.display_result(6)

    # Тест на демонстрацию виртуального вызова
    def test_show_function_result(self) -> None:
        ellipse = Ellipse(a=5, b=3)
        hyperbola = Hyperbola(a=5, b=3)

        # Для эллипса, значение x = 3 должно быть обработано корректно
        show_function_result(ellipse, 3)

        # Для гиперболы, значение x = 6 должно быть обработано корректно
        show_function_result(hyperbola, 6)
