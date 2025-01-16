class Polynomial:

    # konstruktor: przypisywanie współczynników od najniższego stopnia do wielomianu
    def __init__(self, coefficients):
        if isinstance(coefficients, str):
            raise ValueError("Coefficients cannot be a string.")
        if not isinstance(coefficients, list):
            try:
                coefficients = list(coefficients)
            except TypeError:
                raise ValueError("Coefficients must be convertible to a list.")
        if not coefficients:
            coefficients = [0]
        self.coefficients = coefficients
        self._remove_unnecessary_zeros()

    # usuwanie niepotrzebnych zer na końcu wielomianu
    def _remove_unnecessary_zeros(self):
        while len(self.coefficients) > 1 and self.coefficients[-1] == 0:
            self.coefficients.pop()

    # odczyt stopnia wielomianu
    def degree(self):
        return len(self.coefficients) - 1

    # sprawdzanie czy wielomian jest wielomianem zerowym
    def is_zero(self):
        return all(c == 0 for c in self.coefficients)

    # przeciązenie operatora ==
    def __eq__(self, other):
        return (self - other).is_zero()

    # przeciążenie operatora !=
    def __ne__(self, other):
        return not self == other

    # wyświetlanie wielomianu
    def __str__(self):
        if self.is_zero():
            return "0"
        elements = []

        for i in range(self.degree(), -1, -1):
            coeff = self.coefficients[i]
            if coeff == 0:
                continue
            # wyznaczanie znaku
            if isinstance(coeff, complex):
                sign = " - " if coeff.real < 0 else " + " if elements else ""
            else:
                sign = " - " if coeff < 0 else " + " if elements else ""
            # ukrywanie współczynnika "1"
            if isinstance(coeff, complex):
                coeff_str = f"{coeff}"
            else:
                coeff_str = "" if abs(coeff) == 1 and i != 0 else str(abs(coeff))
            if i == 0 and not isinstance(coeff, complex):
                elements.append(f"{sign}{abs(coeff)}")
            elif i== 0 and isinstance(coeff, complex):
                elements.append(f"{sign}{coeff}")
            elif i == 1:
                elements.append(f"{sign}{coeff_str}x")
            else:
                elements.append(f"{sign}{coeff_str}x^{i}")

        return "".join(elements)

    # przeciążenie [] (odczyt współczynnika wielomianu przy danej potędze x)
    def __getitem__(self, index):
            return self.coefficients[index] if index <= self.degree() else 0

    # przeciążenie operatora + (dodawania stałej do wielomianu lub dodawania dwóch wielomianów)
    def __add__(self, other):
        if not isinstance(other, Polynomial):
            other = Polynomial([other])
        max_degree = max(self.degree(), other.degree())
        result_coefficients = [self[i] + other[i] for i in range(max_degree + 1)]
        return Polynomial(result_coefficients)

    def __radd__(self, other):
        return self + other

    # przeciążenie operatora - (odejmowania stałej od wielomianu lub odejmowania dwóch wielomianów)
    def __sub__(self, other):
        if not isinstance(other, Polynomial):
            other = Polynomial([other])
        max_degree = max(self.degree(), other.degree())
        result_coefficients = [self[i] - other[i] for i in range(max_degree + 1)]
        return Polynomial(result_coefficients)

    def __rsub__(self, other):
        return Polynomial([other]) - self

    # przeciążenie operatora * (mnożenia dwóch wielomianów)
    def __mul__(self, other):
        if not isinstance(other, Polynomial):
            other = Polynomial([other])
        result_coefficients = [0] * (self.degree() + other.degree() + 1)
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result_coefficients[i + j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(result_coefficients)

    def __rmul__(self, other):
        return self * other

    # obliczanie wartości wielomianu dla podanej wartości x
    def __call__(self, x):
        result = 0
        for coeff in reversed(self.coefficients):
            result = result * x + coeff
        return result

    # całkowanie wielomianu
    def integrate(self, constant=0):
        new_coefficients = [constant]
        for i in range(self.degree() + 1):
            new_coefficients.append(self[i] / (i + 1))
        return Polynomial(new_coefficients)

    # różniczkowanie wielomianu
    def differentiate(self):
        new_coefficients = []
        for i in range(1, self.degree() + 1):
            new_coefficients.append(self[i] * i)
        return Polynomial(new_coefficients)





"""
Przykład użycia:

p1 = Polynomial([5, -2, 3])
p2 = Polynomial([-1, 7, 2])

print(f"p1 = {p1}")
print(f"p2 = {p2}")
print(f"p1 + p2 = {p1 + p2}")
print(f"p1 - p2 = {p1 - p2}")
print(f"p1 * p2 = {p1 * p2}")
print(f"p1(10) = {p1(10)}")
print(f"p2(10) = {p2(10)}")
"""


