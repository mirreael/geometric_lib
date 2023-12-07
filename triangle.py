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
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_int_area(self):
        res = area(5, 8)
        self.assertEqual(res, 20)

    def test_int_perimeter(self):
        res = perimeter(7, 4, 10)
        self.assertEqual(res, 21)

    def test_float_area(self):
        res = area(3.5, 2.5)
        self.assertEqual(res, 4.375)

    def test_float_perimeter(self):
        res = perimeter(2.5, 2.5, 3.2)
        self.assertEqual(res, 8.2)
    
    def test_incorrect_area(self):
        res = area(-3, 1)
        self.assertEqual(res, 'input error')

    def test_wrong_area(self):
        res = area(1, 13)
        self.assertEqual(300)

    def test_incorrect_perimeter(self):
        res = area(-3, 1, 678)
        self.assertEqual(res, 'input error')

    def test_wrong_perimeter(self):
        res = area(1, 1, 192)
        self.assertEqual(300)

if __name__ == '__main__':
    unittest.main()