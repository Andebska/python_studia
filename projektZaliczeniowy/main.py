
class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients    # od najniższego stopnia
        self._remove_unnecessary_zeros()

    def _remove_unnecessary_zeros(self):         # metoda prywatna
        while len(self.coefficients) > 1 and self.coefficients[-1] == 0:
            self.coefficients.pop()

    def degree(self):
        return len(self.coefficients) - 1

    def is_zero(self):
        return all(c == 0 for c in self.coefficients)

    def __eq__(self, other):           # ==
        return (self - other).is_zero()

    def __ne__(self, other):           # !=
        return not self == other

    def __str__(self):
        elements = []
        for i, coeff in enumerate(self.coefficients):
            if coeff != 0:
                elem = f"{coeff}" if i == 0 else f"{coeff}x^{i}"
                elements.append(elem)
        return " + ".join(reversed(elements)) if elements else 0

    def __getitem__(self, index):     # odczyt współczynnika przy danej potędze
        if index < 0 or index > self.degree():
            return 0
        else:
            return self.coefficients[index]

    def __add__(self, other):
        max_degree = max(self.degree(), other.degree())
        result_coefficients = [self[i] + other[i] for i in range(max_degree + 1)]     
        return Polynomial(result_coefficients)

    def __sub__(self, other):
        max_degree = max(self.degree(), other.degree())
        result_coefficients = [self[i] - other[i] for i in range(max_degree + 1)]
        return Polynomial(result_coefficients)

    def __mul__(self, other):
        result_coefficients = [0] * (self.degree() + other.degree() + 1)
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result_coefficients[i + j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(result_coefficients)

    def __call__(self, x):              # oblicz W(x)
        result = 0
        for coeff in reversed(self.coefficients):
            result = result * x + coeff
        return result



