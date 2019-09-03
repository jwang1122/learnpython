import unittest
from circle import circle_area
from math import pi


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertEqual(circle_area(1), pi)
        self.assertEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1 ** 2)
        self.assertEqual(circle_area(1.2), pi*1.2**2)

    def test_value(self):
        self.assertRaises(ValueError, circle_area, -2)

    def test_type(self):
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError,circle_area, "radius")