import unittest
import calc


class TestCalc(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(calc.add(10, 3), 13)

    def testSub(self):
        self.assertEqual(calc.sub(10, 3), 7)

