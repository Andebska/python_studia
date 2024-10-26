"""
Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3. 
"""

for n in range(31):
    if(n % 3 != 0):
        print(n)