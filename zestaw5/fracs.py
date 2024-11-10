"""
Stworzyć plik fracs.py i zapisać w nim funkcje do działań na ułamkach. Ułamek będzie reprezentowany przez listę
dwóch liczb całkowitych [licznik, mianownik]. Napisać kod testujący moduł fracs. Nie należy korzystać z klasy
Fraction z modułu fractions. Można wykorzystać funkcję fractions.gcd() implementującą algorytm Euklidesa.
# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)

"""

from math import gcd


def simplify(frac):
    licznik, mianownik = frac
    if mianownik < 0:
        licznik, mianownik = - licznik, - mianownik
    nwd = gcd(abs(licznik), abs(mianownik))
    return [licznik // nwd, mianownik // nwd]


def add_frac(frac1, frac2):        # frac1 + frac2
    licznik = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    mianownik = frac1[1] * frac2[1]
    return simplify([licznik, mianownik])


def sub_frac(frac1, frac2):         # frac1 - frac2
    licznik = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    mianownik = frac1[1] * frac2[1]
    return simplify([licznik, mianownik])


def mul_frac(frac1, frac2):         # frac1 * frac2
    licznik = frac1[0] * frac2[0]
    mianownik = frac1[1] * frac2[1]
    return simplify([licznik, mianownik])


def div_frac(frac1, frac2):        # frac1 / frac2
    licznik = frac1[0] * frac2[1]
    mianownik = frac1[1] * frac2[0]
    if mianownik == 0:
        raise ZeroDivisionError("Dzielenie przez zero")
    return simplify([licznik, mianownik])


def is_positive(frac):              # bool, czy dodatni
    return frac[0] > 0 and frac[1] > 0


def is_zero(frac):                  # bool, typu [0, x]
    return frac[0] == 0


def cmp_frac(frac1, frac2):         # -1 | 0 | +1
    licznik1 = frac1[0] * frac2[1]
    licznik2 = frac1[1] * frac2[0]
    if licznik1 < licznik2:
        return -1
    elif licznik1 > licznik2:
        return 1
    else:
        return 0


def frac2float(frac):              # konwersja do float
    return frac[0] / frac[1]
