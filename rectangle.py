import unittest

def area(a, b): 
    """
        Возвращает площадь прямоугольника со стороной a и стороной b
        Параметры:
            а (int) : сторона 
            b (int) : сторона прямоугольника
    """
    return a * b

def perimeter(a, b): 
    """
        Возвращает периметр прямоугольника со стороной a и стороной b
        Параметры:
            а (int) : сторона прямоугольника
            b (int) : сторона прямоугольника
    """
    return 2*a + 2*b

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertAlmostEqual(res, 0, delta=3)

    def test_int_area(self):
        res = area(20, 20)
        self.assertAlmostEqual(res, 400, delta=3)

    def test_float_area(self):
        res = area(2.0, 3.5)
        self.assertAlmostEqual(res, 7.0, delta=3)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            area(-3, -1)

    def test_string_area(self):
        with self.assertRaises(TypeError):
            area('a', 2)


    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertAlmostEqual(res, 0, delta=3)

    def test_int_perimeter(self):
        res = perimeter(10, 10)
        self.assertAlmostEqual(res, 40, delta=3)

    def test_float_perimeter(self):
        res = perimeter(2.5, 3.5)
        self.assertAlmostEqual(res, 12.0, delta=3)

    def test_incorrect_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 1)

    def test_string_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter('a', 2)


if __name__ == '__main__':
    unittest.main()
