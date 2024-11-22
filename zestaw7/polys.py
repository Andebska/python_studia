"""
W pliku polys.py zdefiniować klasę Poly wraz z potrzebnymi metodami. Wykorzystać wyjątek ValueError do obsługi
błędów w wielomianach. Dodać możliwości dodawania liczb (int, long, float) do wielomianów (działania lewostronne i
prawostronne). Dodanie nowych metod kontenerowych i sprawdzenie możliwości iteracji po instancji (for coeff in poly).
Napisać kod testujący moduł polys.
"""

class Poly:
    """Klasa reprezentująca wielomiany."""

    # wg Sedgewicka - tworzymy wielomian c*x^n
    def __init__(self, c=0, n=0):
        if not isinstance(c, (int, float)):
            raise ValueError("Współczynnik c musi być typu int/float")
        if not isinstance(n, int) or n < 0:
            raise ValueError("Stopień wielomianu n musi być nieujemną liczbą całkowitą")
        self.size = n + 1       # rozmiar tablicy
        self.a = self.size * [0]
        self.a[self.size-1] = c

    def __str__(self):
        return str(self.a)

    def __add__(self, other):   # poly1+poly2, poly+liczba
        if isinstance(other, Poly):
            max_len = max(len(self.a), len(other.a))
            result = max_len * [0]
            for i in range(max_len):
                result[i] = (self.a[i] if i < len(self.a) else 0) + (other.a[i] if i < len(other.a) else 0)
            return Poly.create_poly(result)
        elif isinstance(other, (int, float)):
            result = self.a[:]
            result[0] += other
            return Poly.create_poly(result)
        else:
            raise ValueError("Możliwe opcje dodawania: poly1+poly2, poly+liczba")

    __radd__ = __add__  # liczba+poly

    def __sub__(self, other):   # poly1-poly2, poly-liczba
        if isinstance(other, Poly):
            max_len = max(len(self.a), len(other.a))
            result = max_len * [0]
            for i in range(max_len):
                result[i] = (self.a[i] if i < len(self.a) else 0) - (other.a[i] if i < len(other.a) else 0)
            return Poly.create_poly(result)
        elif isinstance(other, (int, float)):
            result = self.a[:]
            result[0] -= other
            return Poly.create_poly(result)
        else:
            raise ValueError("Możliwe opcje odejmowania: poly1-poly2, poly-liczba")

    def __rsub__(self, other):  # liczba-poly
        if isinstance(other, (int, float)):
            result = [-x for x in self.a]
            result[0] += other
            return Poly.create_poly(result)
        else:
            raise ValueError("Nieobsługiwany typ odejmowania")

    def __mul__(self, other):   # poly1*poly2, poly*liczba
        if isinstance(other, Poly):
            result = (len(self.a) + len(other.a) - 1) * [0]
            for i in range(len(self.a)):
                for j in range(len(other.a)):
                    result[i + j] += self.a[i] * other.a[j]
            return Poly.create_poly(result)
        elif isinstance(other, (int, float)):
            result = [coef * other for coef in self.a]
            return Poly.create_poly(result)
        else:
            raise ValueError("Nieobsługiwany typ mnożenia")

    __rmul__ = __mul__  # liczba*poly

    def __pos__(self):          # +poly1 = (+1)*poly1
        return self

    def __neg__(self):          # -poly1 = (-1)*poly1
        return Poly.create_poly([-x for x in self.a])

    def is_zero(self):         # bool, True dla [0], [0, 0],...
        return all(coef == 0 for coef in self.a)

    def __eq__(self, other):    # obsługa poly1 == poly2
        if isinstance(other, Poly):
            return self.a == other.a
        return False

    def __ne__(self, other):        # obsługa poly1 != poly2
        return not self == other

    def eval(self, x):          # schemat Hornera
        if not isinstance(x, (int, float)):
            raise ValueError("Nieobługiwany typ argumentu w eval")
        result = 0
        for coef in reversed(self.a):
            result = result * x + coef
        return result

    def combine(self, other):       # złożenie poly1(poly2(x))
        if not isinstance(other, Poly):
            raise ValueError("Nieobługiwany typ argumentu w combine")
        result = Poly(0, 0)
        for coef in reversed(self.a):
            result = result * other + Poly(coef)
        return result

    def __pow__(self, n):       # poly(x)**n lub pow(poly(x),n)
        if not isinstance(n, int) or n < 0:
            raise ValueError("Wykłądnik potęgu musi być nieujemny i całkowity")
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

    def __len__(self):         # len(poly), rozmiar self.a
        return len(self.a)

    def __getitem__(self, i):     # poly[i], współczynnik przy x^i
        if not isinstance(i, int) or i < 0:
            raise ValueError("Indeks musi być nieujemny i całkowity")
        return self.a[i] if i < len(self.a) else 0

    def __setitem__(self, i, value):      # poly[i] = value
        if not isinstance(i, int) or i < 0:
            raise ValueError("Indeks musi być nieujemny i całkowity")
        if not isinstance(value, (int, float)):
            raise ValueError("Współczynnik musi być liczbą")
        if i >= len(self.a):
            self.a.extend([0] * (i - len(self.a) + 1))
        self.a[i] = value

    def __call__(self, x):     # poly(x)  # dla isinstance(x, (int,long,float)) odpowiada eval(),  # dla isinstance(x, Poly) odpowiada combine()
        if isinstance(x, (int, float)):
            return self.eval(x)
        elif isinstance(x, Poly):
            return self.combine(x)
        else:
            raise ValueError("Nieobsługiwany typ argumentu")


    def __iter__(self):
        return iter(self.a)

    @classmethod
    def create_poly(cls, coefficients):  # tworzenie wielomianu ze współczynników
        while len(coefficients) > 1 and coefficients[-1] == 0:   # usuń zerowe współczynniki
            coefficients.pop()
        poly = cls()
        poly.a = coefficients
        return poly
