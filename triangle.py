import unittest

def area(a, h):
    """
        Возвращает площадь треугольника со стороной a и высотой h
        Параметры:
            а (int) : сторона треугольника
            h (int) : высота h
    """
    return a * h / 2

def perimeter(a, b, c):
    """
        Возвращает периметр треугольника со сторонами a, b, c
        Параметры:
            a (int) : сторона треугольника
            b (int) : сторона треугольника
            c (int) : сторона треугольника
    """
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 0)
        self.assertAlmostEqual(res, 0, delta=3)

    def test_int_area(self):
        res = area(5, 8)
        self.assertAlmostEqual(res, 20, delta=3)

    def test_float_area(self):
        res = area(3.5, 2.5)
        self.assertAlmostEqual(res, 4.375, delta=3)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            area(-3, -1)

    def test_string_area(self):
        with self.assertRaises(TypeError):
            area('a', 1)

    

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertAlmostEqual(res, 0, delta=3)

    def test_int_perimeter(self):
        res = perimeter(7, 4, 10)
        self.assertAlmostEqual(res, 21, delta=3)

    def test_float_perimeter(self):
        res = perimeter(2.5, 2.5, 3.2)
        self.assertAlmostEqual(res, 8.2, delta=3)

    def test_incorrect_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 1, 2)

    def test_string_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter('a', 0, 1)


if __name__ == '__main__':
    unittest.main()
