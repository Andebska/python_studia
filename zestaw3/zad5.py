"""
Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo obsłużyć liczby składające się z kilku cyfr
(ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). Należy zbudować pełny string, a potem go wypisać.

|....|....|....|....|....|....|....|....|....|....|....|....|
0    1    2    3    4    5    6    7    8    9   10   11   12

"""

length = int(input("wprowadź wybraną długość"))
marks = "|"
numbers = "0"

for l in range(1, length+1):
    marks += "....|"
    numbers += f"{l:5}"              #dla każdej liczby ustawia jej długość na 5 (jeśli jest mniejsza- dodaje spacje)


print(marks)
print(numbers)