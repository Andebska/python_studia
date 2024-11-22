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
        self.assertEqual(p1 + 5, Poly.create_poly([6, 2]))
        self.assertEqual(5 + p1, Poly.create_poly([6, 2]))

    def test_sub(self):
        p1 = Poly.create_poly([1, 2])
        p2 = Poly.create_poly([3, 4, 5])
        self.assertEqual(p1 - p2, Poly.create_poly([-2, -2, -5]))
        self.assertEqual(p1 - 5, Poly.create_poly([-4, 2]))
        self.assertEqual(5 - p1, Poly.create_poly([4, -2]))

    def test_mul(self):
        p1 = Poly.create_poly([1, 2])
        p2 = Poly.create_poly([2, 3])
        self.assertEqual(p1 * p2, Poly.create_poly([2, 7, 6]))
        self.assertEqual(p1 * 2, Poly.create_poly([2, 4]))
        self.assertEqual(2 * p1, Poly.create_poly([2, 4]))

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

    def test_call(self):
        p1 = Poly.create_poly([1, 2, 3])
        self.assertEqual(p1(2), 17)
        p2 = Poly.create_poly([0, 1])
        self.assertEqual(p1(p2), Poly.create_poly([1, 2, 3]))

    def test_container_operations(self):
        p = Poly.create_poly([1, 2, 3])
        self.assertEqual(len(p), 3)
        self.assertEqual(p[1], 2)
        p[2] = 7
        self.assertEqual(p[2], 7)
        self.assertEqual(p, Poly.create_poly([1, 2, 7]))

    def test_iter(self):
        p = Poly.create_poly([1, 2, 3])
        coeffs = [coef for coef in p]
        self.assertEqual(coeffs, [1, 2, 3])

    def test_exceptions(self):
        with self.assertRaises(ValueError):
            Poly("string", 2)
        with self.assertRaises(ValueError):
            Poly(2, -3)
        with self.assertRaises(ValueError):
            p = Poly.create_poly([1, 2, 3])
            p["string"] = 4


if __name__ == '__main__':
    unittest.main()