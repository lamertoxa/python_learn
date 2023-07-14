import unittest
from math import sqrt

def quadratic_equation(a, b, c):
    D = (b ** 2) - 4 * a * c
    try:
        if D==0:
            return -b/(2*a)
        x2 = (-b - sqrt(D)) / (2 * a)
        x1 = (-b + sqrt(D)) / (2 * a)
    except ZeroDivisionError:
        raise ValueError
    except ValueError:
        return None

    return (x1,x2)

class QuadraticEquationTest(unittest.TestCase):
    def test_discriminant_positive(self):
        expect = (1.0,-3.0)
        result = quadratic_equation(1,2,-3)
        self.assertEqual(expect,result)
    def test_discriminantrand_val(self):
        expect = (0.5,-2.0)
        result = quadratic_equation(2,3,-2)
        self.assertEqual(expect,result)

    def test_discriminant_negative(self):
        result = quadratic_equation(3,4,3)
        self.assertEqual(None,result)
    def test_discriminant_zero(self):
        expect = -1
        result = quadratic_equation(3, 6, 3)
        self.assertEqual(expect, result)

