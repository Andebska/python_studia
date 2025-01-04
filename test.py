import unittest
from main import *


class TestPolynomial(unittest.TestCase):
    def test_degree(self):
        p = Polynomial([1, 0, 2])     # 1 + 2x^2
        self.assertEqual(p.degree(),2)

    def test_is_zero(self):
        p = Polynomial([0, 0, 0])
        self.assertTrue(p.is_zero())

    def test_eq(self):
        p1 = Polynomial([1, 2, 0])
        p2 = Polynomial([1, 2])
        self.assertEqual(p1, p2)

    def test_ne(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([1, 3, 2])
        self.assertNotEqual(p1, p2)

    def test_str(self):
        p = Polynomial([1, 2, 3])
        self.assertEqual(str(p), "3x^2 + 2x^1 + 1")

    def test_getitem(self):
        p = Polynomial([5, 3, 7])       # 5 + 3x + 7x^2
        self.assertEqual(p.__getitem__(2), 7)

    def test_add(self):
        p1 = Polynomial([1, 2, 3])     # 1 + 2x + 3x^2
        p2 = Polynomial([3, 4, 0])     # 3 + 4x
        self.assertEqual(p1 + p2, Polynomial([4, 6, 3]))

    def test_sub(self):
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([3, 4, 0])
        self.assertEqual(p1 - p2, Polynomial([-2, -2, 3]))

    def test_mul(self):
        p1 = Polynomial([1, 1])      # 1 + x
        p2 = Polynomial([1, -1])     # 1 - x
        self.assertEqual(p1 * p2, Polynomial([1, 0, -1]))

    def test_call(self):
        p = Polynomial([1, 2, 3])   # 1 + 2x + 3x^2
        self.assertEqual(p(2), 17)


if __name__ == '__main__':
    unittest.main()