import pytest
from math import isclose
from src.individual_task_2 import Ellipse, Hyperbola, show_function_result


class TestFunction:
    def test_ellipse_calculate_y(self):
        ellipse = Ellipse(a=5, b=3)

        y = ellipse.calculate_y(3)
        assert isclose(y, 2.4, rel_tol=1e-2)

        y = ellipse.calculate_y(0)
        assert y == 3

        with pytest.raises(ValueError):
            ellipse.calculate_y(6)

    def test_hyperbola_calculate_y(self):
        hyperbola = Hyperbola(a=5, b=3)

        y = hyperbola.calculate_y(6)
        assert isclose(y, 1.98, rel_tol=1e-2)

        with pytest.raises(ValueError):
            hyperbola.calculate_y(3)

    def test_display_result_ellipse(self):
        ellipse = Ellipse(a=5, b=3)

        with pytest.raises(ValueError):
            ellipse.display_result(6)

        ellipse.display_result(2)

    def test_display_result_hyperbola(self):
        hyperbola = Hyperbola(a=5, b=3)

        with pytest.raises(ValueError):
            hyperbola.display_result(3)

        hyperbola.display_result(6)

    def test_show_function_result(self):
        ellipse = Ellipse(a=5, b=3)
        hyperbola = Hyperbola(a=5, b=3)

        show_function_result(ellipse, 3)

        show_function_result(hyperbola, 6)
