"""
Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię:
(rekurencyjnie)
def factorial(n):
    Rekurencyjne obliczanie funkcji silnia n!
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

"""

def factorial(n):
    if n < 0:
        raise ValueError("Nie definiujemy silni dla liczb ujemnych ")

    result = 1
    for i in range (2, n + 1):
        result *= i
    return result


print(factorial(5))