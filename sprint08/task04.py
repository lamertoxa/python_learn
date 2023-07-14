import unittest
import coverage
from math import sqrt
valid_test_data = [
    ((3, 4, 5), 6.0),
    ((10, 10, 10), 43.30),
    ((6, 7, 8), 20.33),
    ((7, 7, 7), 21.21),
    ((50, 50, 75), 1240.19),
    ((37, 43, 22), 406.99),
    ((26, 25, 3), 36.0),
    ((30, 29, 5), 72.0),
    ((87, 55, 34), 396.0),
    ((120, 109, 13), 396.0),
    ((123, 122, 5), 300.0)
]
not_valid_triangle = [
    (1, 2, 3),
    (1, 1, 2),
    (7, 7, 15),
    (100, 7, 90),
    (17, 18, 35),
    (127, 17, 33),
    (145, 166, 700),
    (1000, 2000, 1),
    (717, 17, 7),
    (0, 7, 7),
    (-7, 7, 7)
]
not_valid_arguments = [
    ('3', 4, 5),
    ('a', 2, 3),
    (7, "str", 7),
    ('1', '1', '1'),
    'string',
    (7, 2),
    (7, 7, 7, 7),
    'str',
    10,
    ('a', 'str', 7)
]


class TriangleNotValidArgumentException(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return self.data

class TriangleNotExistException(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return self.data


class Triangle:
    def __init__(self, numbers):
        try:
            self.a, self.b, self.c = [i  for i in numbers ]
        except (TypeError,ValueError):
            raise TriangleNotValidArgumentException("Not valid arguments")
        try:
            if self.a <=0 or self.b <=0 or self.c <=0:
                raise TriangleNotExistException("Can`t create triangle with this arguments")
        except TypeError:
            raise TriangleNotValidArgumentException("Not valid arguments")
        p = (self.a + self.b + self.c) / 2
        try:
            self.result = float("%.2f" % sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)))
        except ValueError:
            raise TriangleNotExistException("Can`t create triangle with this arguments")
        if self.result <= 0:
            raise TriangleNotExistException("Can`t create triangle with this arguments")


    def get_area(self):

        return self.result



class TriangleTest(unittest.TestCase):
    def test_triangle_valid(self):
        for test in valid_test_data:
            with self.subTest():
                obj = Triangle(test[0])
                self.assertAlmostEqual(test[1],obj.get_area(),delta=1)
    def test_triangle_invalid(self):
        for test in not_valid_triangle:
            with self.subTest():
                with self.assertRaises(TriangleNotExistException):
                    obj = Triangle(test)
                    obj.get_area()

    def test_triangle_invalidArg(self):
        for test in not_valid_arguments:
            with self.subTest():
                with self.assertRaises(TriangleNotValidArgumentException):
                    obj = Triangle(test)
                    obj.get_area()