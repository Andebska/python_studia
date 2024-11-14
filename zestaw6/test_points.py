# Kod testujący moduł.

import unittest
from points import *

class TestPoint(unittest.TestCase):

    def test_str(self):
        self.assertEqual(str(Point(1, 2)), "(1, 2)")

    def test_repr(self):
        self.assertEqual(repr(Point(1, 2)), "Point(1, 2)")

    def test_eq(self):
        self.assertTrue(Point(1, 2) == Point(1, 2))
        self.assertFalse(Point(1, 2) == Point(3, 4))

    def test_ne(self):
        self.assertTrue(Point(1, 2) != Point(3, 4))
        self.assertFalse(Point(1, 2) != Point(1, 2))

    def test_add(self):
        self.assertEqual(Point(1, 2) + Point(3, 4), Point(4, 6))

    def test_sub(self):
        self.assertEqual(Point(3, 4) - Point(1, 2), Point(2, 2))

    def test_mul(self):
        self.assertEqual(Point(1, 2) * Point(3, 4), 11)

    def test_cross(self):
        self.assertEqual(Point(1, 2).cross(Point(3, 4)), -2)

    def test_length(self):
        self.assertEqual(Point(3, 4).length(), 5.0)

    def test_hash(self):
        self.assertEqual(hash(Point(1, 2)), hash((1, 2)))
        self.assertNotEqual(hash(Point(1, 2)), hash(Point(2, 1)))


if __name__ == '__main__':
    unittest.main()