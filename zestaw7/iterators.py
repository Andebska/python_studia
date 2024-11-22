"""
Stworzyć następujące iteratory nieskończone:
(a) zwracający 0, 1, 0, 1, 0, 1, ...,
(b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D],
(c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia].
"""


import itertools
import random

# a:

def iterator_a():
    return itertools.cycle([0, 1])


iter_a = iterator_a()
for i in range(21):
    print(next(iter_a), end=" ")

print()
# b:

def iterator_b():
    values = ["N", "E", "S", "W"]
    return (random.choice(values) for i in itertools.count())

iter_b = iterator_b()
for i in range(21):
    print(next(iter_b), end=" ")

print()
# c:

def iterator_c():
    return itertools.cycle(range(7))


iter_c = iterator_c()
for i in range(21):
    print(next(iter_c), end=" ")