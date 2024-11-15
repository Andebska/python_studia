"""
W pliku polys.py zdefiniować klasę Poly wraz z potrzebnymi metodami. Wielomian będzie reprezentowany przez
listę swoich współczynników, [a0, a1, a2] dla a0 + a1 * x + a2 * x * x. Wielomiany mogą mieć dowolnie
wysoki stopień. Napisać kod testujący moduł polys.
"""

class Poly:
    """Klasa reprezentująca wielomiany."""

    # wg Sedgewicka - tworzymy wielomian c*x^n
    def __init__(self, c=0, n=0):
        self.size = n + 1       # rozmiar tablicy
        self.a = self.size * [0]
        self.a[self.size-1] = c

    def __str__(self):
        return str(self.a)

    def __add__(self, other):   # poly1 + poly2
        max_len = max(len(self.a), len(other.a))
        result = max_len * [0]
        for i in range(max_len):
            result[i] = (self.a[i] if i < len(self.a) else 0) + (other.a[i] if i < len(other.a) else 0)
        return Poly.create_poly(result)

    def __sub__(self, other):   # poly1 - poly2
        max_len = max(len(self.a), len(other.a))
        result = max_len * [0]
        for i in range(max_len):
            result[i] = (self.a[i] if i < len(self.a) else 0) - (other.a[i] if i < len(other.a) else 0)
        return Poly.create_poly(result)

    def __mul__(self, other):   # poly1 * poly2
        result = (len(self.a) + len(other.a) - 1) * [0]
        for i in range(len(self.a)):
            for j in range(len(other.a)):
                result[i + j] += self.a[i] * other.a[j]
        return Poly.create_poly(result)

    def __pos__(self):          # +poly1 = (+1)*poly1
        return self

    def __neg__(self):          # -poly1 = (-1)*poly1
        return Poly.create_poly([-x for x in self.a])

    def __eq__(self, other):    # obsługa poly1 == poly2
        return self.a == other.a

    def __ne__(self, other):        # obsługa poly1 != poly2
        return not self == other

    def eval(self, x):          # schemat Hornera
        result = 0
        for coef in reversed(self.a):
            result = result * x + coef
        return result

    def combine(self, other):       # złożenie poly1(poly2(x))
        result = Poly(0, 0)
        for coef in reversed(self.a):
            result = result * other + Poly(coef)
        return result

    def __pow__(self, n):       # poly(x)**n lub pow(poly(x),n)
        result = Poly(1, 0)
        for i in range(n):
            result *= self
        return result

    def diff(self):             # różniczkowanie
        if len(self.a) == 1:
            return Poly(0, 0)
        result = [i * self.a[i] for i in range(1, len(self.a))]
        return Poly.create_poly(result)

    def integrate(self):        # całkowanie
        result = (len(self.a) + 1) * [0]
        for i in range(len(self.a)):
            result[i + 1] = self.a[i] / (i + 1)
        return Poly.create_poly(result)

    def is_zero(self):         # bool, True dla [0], [0, 0],...
        return all(coef == 0 for coef in self.a)

    @staticmethod
    def create_poly(coefficients):  # tworzenie wielomianu ze współczynników
        while len(coefficients) > 1 and coefficients[-1] == 0:   # usuń zerowe współczynniki
            coefficients.pop()
        poly = Poly()
        poly.a = coefficients
        return poly
