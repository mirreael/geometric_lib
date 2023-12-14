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
        self.assertAlmostEqual(res, 0, delta=3)
    
    def test_int_area(self):
        res = area(10)
        self.assertAlmostEqual(res, 314.159, delta=3)
    
    def test_float_area(self):
        res = area(2.3)
        self.assertAlmostEqual(res, 16.619, delta=3)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            area(-6)
    
    def test_string_area(self):
        with self.assertRaises(TypeError):
            area('a')


    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertAlmostEqual(res, 0, delta=3)

    def test_int_perimeter(self):
        res = perimeter(10)
        self.assertAlmostEqual(res, 62.832, delta=3)

    def test_float_perimeter(self):
        res = perimeter(1.5)
        self.assertAlmostEqual(res, 9.425, delta=3)

    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-9)

    
    def test_string_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter('a')
    
    

if __name__ == '__main__':
    unittest.main()