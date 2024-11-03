"""
Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do
right włącznie. Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.
"""

def odwracanie_iteracyjne(L, left, right):
    while(left < right):
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
    return L

def odwracanie_rekurencyjne(L, left, right):
    if left >= right:
        return L

    L[left], L[right] = L[right], L[left]
    return odwracanie_rekurencyjne(L, left + 1, right - 1)


L1 = [1, 3, 7, 4, 9, 2, 6]
L2 = [1, 3, 7, 4, 9, 2, 6]
print("L = [1, 3, 7, 4, 9, 2, 6]\nleft=2, right=5\n")
print("Iteracyjnie: ", odwracanie_iteracyjne(L1, 2, 5))
print("\nRekurencyjnie: ", odwracanie_rekurencyjne(L2, 2, 5))



