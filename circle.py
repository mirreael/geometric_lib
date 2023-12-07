import math
import unittest


def area(r):
    """
        Возвращает площадь круга с радиусом r
        Параметр:
            r (int) : радиус окружности
    """
    return math.pi * r * r


def perimeter(r):
    """
        Возвращает периметр круга с радиусом r
        Параметр:
            r (int) : радиус окружности
    """
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_int_area(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)

    def test_int_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)

    def test_float_area(self):
        res = area(2.3)
        self.assertEqual(res, 16.619025137490002)

    def test_float_perimeter(self):
        res = perimeter(1.5)
        self.assertEqual(res, 9.42477796076938)

    def test_incorrect_area(self):
        res = area(-6)
        self.assertEqual(res, 'input error')

    def test_wrong_area(self):
        res = area(1)
        self.assertEqual(300, 2341)

    def test_incorrect_perimeter(self):
        res = area(-9)
        self.assertEqual(res, 'input error')

    def test_wrong_perimeter(self):
        res = area(4)
        self.assertEqual(300, 2234)

if __name__ == '__main__':
    unittest.main()