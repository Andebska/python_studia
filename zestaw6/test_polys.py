# Kod testujący moduł.

import unittest
from polys import *

class TestPoly(unittest.TestCase):
    def test_str(self):
        p = Poly.create_poly([1, 2, 3])
        self.assertEqual(str(p), "[1, 2, 3]")

    def test_add(self):
        p1 = Poly.create_poly([1, 2])
        p2 = Poly.create_poly([3, 4, 5])
        self.assertEqual(p1 + p2, Poly.create_poly([4, 6, 5]))

    def test_sub(self):
        p1 = Poly.create_poly([1, 2])
        p2 = Poly.create_poly([3, 4, 5])
        self.assertEqual(p1 - p2, Poly.create_poly([-2, -2, -5]))

    def test_mul(self):
        p1 = Poly.create_poly([1, 2])
        p2 = Poly.create_poly([2, 3])
        self.assertEqual(p1 * p2, Poly.create_poly([2, 7, 6]))

    def test_pos(self):
        p = Poly.create_poly([1, -2])
        self.assertEqual(+p, Poly.create_poly([1, -2]))

    def test_neg(self):
        p = Poly.create_poly([1, -2])
        self.assertEqual(-p, Poly.create_poly([-1, 2]))

    def test_eq(self):
        p1 = Poly.create_poly([1, 2])
        p2 = Poly.create_poly([1, 2])
        self.assertEqual(p1, p2)

    def test_ne(self):
        p1 = Poly.create_poly([1, 2])
        p2 = Poly.create_poly([1, 3])
        self.assertNotEqual(p1, p2)

    def test_eval(self):
        p = Poly.create_poly([1, 2, 3])
        self.assertEqual(p.eval(2), 17)

    def test_combine(self):
        p1 = Poly.create_poly([1, 2])
        p2 = Poly.create_poly([0, 1])
        self.assertEqual(p1.combine(p2), Poly.create_poly([1, 2]))

    def test_pow(self):
        p = Poly.create_poly([1, 1])
        self.assertEqual(p ** 2, Poly.create_poly([1, 2, 1]))

    def test_diff(self):
        p = Poly.create_poly([1, 2, 3])
        self.assertEqual(p.diff(), Poly.create_poly([2, 6]))

    def test_integrate(self):
        p = Poly.create_poly([1, 4])
        self.assertEqual(p.integrate(), Poly.create_poly([0, 1, 2]))

    def test_is_zero(self):
        p1 = Poly.create_poly([0, 0, 0])
        p2 = Poly.create_poly([0, 0, 1])
        self.assertTrue(p1.is_zero())
        self.assertFalse(p2.is_zero())


if __name__ == '__main__':
    unittest.main()