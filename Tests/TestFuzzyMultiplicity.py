__author__ = 'bombastic'

import unittest

from FuzzyNumber import *
from FuzzyPoint import *
from FuzzyMultiplicity import *


class TestFuzzyMultiplicity(unittest.TestCase):

    def setUp(self):
        pass

    def generate_test_multiplicity(self):
        fuzzy_a = FuzzyNumber()
        fuzzy_a.insert(FuzzyPoint(1, 0))
        fuzzy_a.insert(FuzzyPoint(2, 1))
        fuzzy_a.insert(FuzzyPoint(3, 0))
        fuzzy_b = FuzzyNumber()
        fuzzy_b.insert(FuzzyPoint(4, 0.25))
        fuzzy_b.insert(FuzzyPoint(5, 1))
        fuzzy_b.insert(FuzzyPoint(6, 0.75))
        return FuzzyMultiplicity(fuzzy_a, fuzzy_b)

    def test_get_func_of_belonging(self):
        fuzzy_multiplicity = self.generate_test_multiplicity()
        self.assertEqual(fuzzy_multiplicity.get_func_of_belonging(1.5, 4.5), 0.5625)

    def test_get_key_points(self):
        fuzzy_multiplicity = self.generate_test_multiplicity()
        self.assertEqual(
            fuzzy_multiplicity.get_key_points(),
            [
                (1, 4),
                (1, 5),
                (1, 6),
                (2, 4),
                (2, 5),
                (2, 6),
                (3, 4),
                (3, 5),
                (3, 6)
            ]
        )

    def test_get_straight_key_points(self):
        fuzzy_multiplicity = self.generate_test_multiplicity()
        self.assertEqual(fuzzy_multiplicity.get_straight_key_points((1,4), 1), [(1, 4), (2, 5), (3, 6)])