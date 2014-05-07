import unittest

from FuzzyNumber import *
from FuzzyPoint import *


class TestFuzzyNumber(unittest.TestCase):

    def setUp(self):
        pass

    def test_interpolation(self):
        number = FuzzyNumber()
        number.insert(FuzzyPoint(0, 0.5))
        self.assertEqual(number.get(0), FuzzyPoint(0, 0.5))

        number.insert(FuzzyPoint(1, 1))
        self.assertEqual(number.get(0.5), FuzzyPoint(0.5, 0.75))

    def test_normalization(self):
        number = FuzzyNumber()
        number.insert(FuzzyPoint(0, 0))
        number.insert(FuzzyPoint(1, 1))
        self.assertEqual(number.get_square(), 0.5)

        number.insert(FuzzyPoint(2, 1))

        number.normalize()
        self.assertEqual(number.get_square(), 1)