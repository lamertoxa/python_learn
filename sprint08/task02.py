import unittest


def divide(num1, num2):
    return float(num1) / num2


class DivideTest(unittest.TestCase):
    def test_zero_numerator(self):
        expected = 0
        result = divide(0, 1)
        self.assertEqual(expected, result)

    def test_raises(self):
        self.assertRaises(ZeroDivisionError, divide, 5000, 0)

    def test_int_divide(self):
        expected = 50.0
        result = divide(100, 2)
        self.assertEqual(expected, result)

    def test_float_divide(self):
        expected = 5.125
        result = divide(20.5, 4)
        self.assertEqual(expected, result)