"""
Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string,
 a potem go wypisać. Przykładowy prostokąt składający się 2x4 pól ma postać:

+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+

"""

height = int(input("Podaj wybraną wysokość (ilość kratek): "))
width = int(input("Podaj wybraną długość (ilość kratek): "))

for n in range(height):
    print("+" + "---+" * width)
    print("|" + "   |" * width)

print("+" + "---+" * width)

