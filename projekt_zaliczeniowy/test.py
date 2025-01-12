import unittest
from Polynomial import *

class TestPolynomial(unittest.TestCase):
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            Polynomial("str")
        with self.assertRaises(ValueError):
            Polynomial([1, "str", 3])

    def test_degree(self):
        p1 = Polynomial([1, 0, 2])     # 1 + 2x^2
        p2 = Polynomial([0])
        self.assertEqual(p1.degree(),2)
        self.assertEqual(p2.degree(), 0)

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
        p1 = Polynomial([1, 2, 3])
        p2 = Polynomial([-1, -3, 4])
        p3 = Polynomial([0, 0, 3])
        self.assertEqual(str(p1), "3x^2 + 2x + 1")
        self.assertEqual(str(p2), "4x^2 - 3x - 1")
        self.assertEqual(str(p3), "3x^2")

    def test_getitem(self):
        p = Polynomial([5, 3, 7])       # 5 + 3x + 7x^2
        self.assertEqual(p[2], 7)
        self.assertEqual(p[100], 0)
        with self.assertRaises(IndexError):
            _ = p[-5]

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
        p3 = Polynomial([0])
        self.assertEqual(p1 * p2, Polynomial([1, 0, -1]))
        self.assertEqual(p1 * p3, Polynomial([0]))

    def test_call(self):
        p1 = Polynomial([1, 2, 3])   # 1 + 2x + 3x^2
        p2 = Polynomial([-1, -2, 3])    # -1 -2x + 3x^2
        self.assertEqual(p1(0), 1)
        self.assertEqual(p1(2), 17)
        self.assertEqual(p2(0), -1)
        self.assertEqual(p2(2), 7)


if __name__ == '__main__':
    unittest.main()