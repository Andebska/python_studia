"""
Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która może zawierać zagnieżdżone podsekwencje.
Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element jest sekwencją, wykonać przez isinstance(item, (list, tuple)).
"""

def sum_seq(sequence):
    result = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result += sum_seq(item)
        elif isinstance(item, (int, float)):
            result += item
    return result


print("Sekwencja: [1, 2, 3, 4, 5], Wynik: ", sum_seq([1, 2, 3, 4, 5]))
print("Sekwencja: [1, [2, 3], 4, [5, [6,7]]], Wynik: ", sum_seq([1, [2, 3], 4, [5, [6,7]]]))
print("Sekwencja: ((1, 2), 3, (4, (5, 6)), 7), Wynik: ", sum_seq(((1, 2), 3, (4, (5, 6)), 7)))
print("Sekwencja: [1.25, (2, [3, 4.5], 5), 6], Wynik: ", sum_seq([1.25, (2, [3, 4.5], 5), 6]))
print("Sekwencja: [1, 2, \"kot\", 3], Wynik: ", sum_seq([1, 2, "kot", 3]))
