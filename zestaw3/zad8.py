"""
Dla dwóch sekwencji liczb lub znaków znaleźć: (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń),
(b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).
"""

L1 = [1, 2, 6, 7, 3, 2, 2]
L2 = [0, 5, 7, 2, 8, 8]

print(f"L1: {L1}")
print(f"L2: {L2}")
#zamienia na zbiory (elementy nie będą się powtarzać) i liczy przecięcie:
print(f"Lista elementów występujących jednocześnie w L1 i L2: {list(set(L1) & set(L2))}")
#zamienia na zbiory (elementy nie będą się powtarzać) i liczy sumę:
print(f"Lista elementów występujących łącznie w L1 i L2: {list(set(L1) | set(L2))}")

print()
S1 = "abrakadabra"
S2 = "samochód"
print(f"S1: {S1}")
print(f"S2: {S2}")
print(f"Lista liter występujących jednocześnie w S1 i S2: {list(set(S1) & set(S2))}")
print(f"Lista liter występujących łącznie w S1 i S2: {list(set(S1) | set(S2))}")
