"""
Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego
(rekurencyjnie)
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
"""

def fibonacci(n):
    if n < 0:
        raise ValueError("Ciąg Fibonacciego nie jest zdefiniowany dla liczb ujemnych")
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    x, y = 0, 1
    for i in range(2, n + 1):
        x, y = y, x + y
    return y


print(fibonacci(12))