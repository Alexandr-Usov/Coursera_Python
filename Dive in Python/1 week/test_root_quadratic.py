"""Тест для проверки модуля решения квадратных уравнений"""

import unittest
import root_qadratic


class TestRoot(unittest.TestCase):
    def test_root_quadratic(self):
        self.assertEqual(root_qadratic.root_calc(1, -3, -4), [-1, 4])


if __name__ == "__main__":
    t = TestRoot()
    t.test_root_quadratic()
