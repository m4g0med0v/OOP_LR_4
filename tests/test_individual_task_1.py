import pytest
from math import isclose
from src.individual_task_1 import RightAngled, Triangle


class TestTriangle:
    def test_triangle_creation(self):
        triangle = Triangle(3, 4, 5)
        assert triangle.a == 3
        assert triangle.b == 4
        assert triangle.c == 5

    def test_invalid_triangle_creation(self):
        with pytest.raises(ValueError):
            Triangle(1, 2, 10)

    def test_set_sides(self):
        triangle = Triangle(3, 4, 5)
        triangle.set_sides(6, 8, 10)
        assert triangle.a == 6
        assert triangle.b == 8
        assert triangle.c == 10

    def test_perimeter(self):
        triangle = Triangle(3, 4, 5)
        assert triangle.perimeter() == 12

    def test_angles(self):
        triangle = Triangle(3, 4, 5)
        angles = triangle.angles()
        assert isclose(angles[0], 36.87, rel_tol=1e-2)
        assert isclose(angles[1], 53.13, rel_tol=1e-2)
        assert isclose(angles[2], 90.00, rel_tol=1e-2)


class TestRightAngled:
    def test_rightangled_creation(self):
        triangle = RightAngled(3, 4)
        assert triangle.a == 3
        assert triangle.b == 4
        assert isclose(triangle.c, 5, rel_tol=1e-2)

    def test_area(self):
        triangle = RightAngled(3, 4)
        assert triangle.area == 6.0

    def test_perimeter(self):
        triangle = RightAngled(3, 4)
        assert triangle.perimeter() == 12

    def test_angles(self):
        triangle = RightAngled(3, 4)
        angles = triangle.angles()
        assert isclose(angles[0], 36.87, rel_tol=1e-2)
        assert isclose(angles[1], 53.13, rel_tol=1e-2)
        assert isclose(angles[2], 90.00, rel_tol=1e-2)
