"""
Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo obsłużyć liczby składające się z kilku cyfr
(ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). Należy zbudować pełny string, a potem go wypisać.

|....|....|....|....|....|....|....|....|....|....|....|....|
0    1    2    3    4    5    6    7    8    9   10   11   12

"""
def make_ruler(n):
    length = int(n)
    marks = "|"
    numbers = "0"

    for l in range(1, length + 1):
        marks += "....|"
        numbers += f"{l:5}"  # dla każdej liczby ustawia jej długość na 5 (jeśli jest mniejsza- dodaje spacje)

    result = marks + '\n' + numbers
    return result


print(make_ruler(14))


"""
Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string,
 a potem go wypisać. Przykładowy prostokąt składający się 2x4 pól ma postać:

+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+

"""

def make_grid(rows, cols):
    result = ""

    for n in range(rows):
        result += "+" + "---+" * cols + '\n'
        result += "|" + "   |" * cols + '\n'

    result += "+" + "---+" * cols
    return result


print()
print(make_grid(3, 5))