
"""
L = [3, 5, 4] ; L = L.sort()
sort() modyfikuje oryginalną listę, więc nie musimy jej osobno przypisywać
"""
#poprawnie:
L = [3, 5, 4]
L.sort()
print(L)

"""
x, y = 1, 2, 3
nie można przypisać trzech wartości do tylko dwóch zmiennych
"""
#poprawnie:
x, y, z = 1, 2, 3
print(x, y, z)

"""
X = 1, 2, 3 ; X[1] = 4
X jest krotką, więc nie można zmieniać jego wartości
"""
#poprawnie:
X = [1, 2, 3]
X[1] = 4
print(X[1])

"""
X = [1, 2, 3] ; X[3] = 4
W liście nie ma elementu o indeksie 3, są numerowane od 0 do 2
"""
#poprawnie:
Y = [1, 2, 3]
Y[2] = 4
print(Y[2])
#lub:
Z = [1, 2, 3]
Z.append(4)
print(Z[3])

"""
X = "abc" ; X.append("d")
metoda append nie działa ze stringiem 
"""
#poprawnie:
A = "abc"
A += "d"
print(A)

"""
L = list(map(pow, range(8)))
funkcja pow wymaga dwóch argumentów
"""
#poprawnie:
B = list(map(pow, range(8), [2] * 8))
print(B)
