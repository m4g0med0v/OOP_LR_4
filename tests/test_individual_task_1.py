import unittest
from math import isclose

from src.individual_task_1 import RightAngled, Triangle


class TestTriangle(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print(f"{cls.__name__:=^80}")

    @classmethod
    def tearDownClass(cls) -> None:
        print("=" * 80)

    # Тест на создание валидного треугольника
    def test_triangle_creation(self) -> None:
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.a, 3)
        self.assertEqual(triangle.b, 4)
        self.assertEqual(triangle.c, 5)

    # Проверка, что ValueError выбрасывается для невалидных сторон
    def test_invalid_triangle_creation(self) -> None:
        with self.assertRaises(ValueError):
            Triangle(1, 2, 10)

    # Проверка изменения сторон треугольника
    def test_set_sides(self) -> None:
        triangle = Triangle(3, 4, 5)
        triangle.set_sides(6, 8, 10)
        self.assertEqual(triangle.a, 6)
        self.assertEqual(triangle.b, 8)
        self.assertEqual(triangle.c, 10)

    # Проверка вычисления периметра
    def test_perimeter(self) -> None:
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.perimeter(), 12)

    # Проверка вычисления углов
    def test_angles(self) -> None:
        triangle = Triangle(3, 4, 5)
        angles = triangle.angles()
        self.assertTrue(isclose(angles[0], 36.87, rel_tol=1e-2))
        self.assertTrue(isclose(angles[1], 53.13, rel_tol=1e-2))
        self.assertTrue(isclose(angles[2], 90.00, rel_tol=1e-2))


class TestRightAngled(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print(f"{cls.__name__:=^80}")

    @classmethod
    def tearDownClass(cls) -> None:
        print("=" * 80)

    # Тест на создание прямоугольного треугольника
    def test_rightangled_creation(self) -> None:
        triangle = RightAngled(3, 4)
        self.assertEqual(triangle.a, 3)
        self.assertEqual(triangle.b, 4)
        self.assertTrue(isclose(triangle.c, 5, rel_tol=1e-2))

    # Проверка вычисления площади
    def test_area(self) -> None:
        triangle = RightAngled(3, 4)
        self.assertEqual(triangle.area, 6.0)

    # Проверка периметра для прямоугольного треугольника
    def test_perimeter(self) -> None:
        triangle = RightAngled(3, 4)
        self.assertEqual(triangle.perimeter(), 12)

    # Проверка углов для прямоугольного треугольника
    def test_angles(self) -> None:
        triangle = RightAngled(3, 4)
        angles = triangle.angles()
        self.assertTrue(isclose(angles[0], 36.87, rel_tol=1e-2))
        self.assertTrue(isclose(angles[1], 53.13, rel_tol=1e-2))
        self.assertTrue(isclose(angles[2], 90.00, rel_tol=1e-2))
        self.assertTrue(isclose(angles[2], 90.00, rel_tol=1e-2))
