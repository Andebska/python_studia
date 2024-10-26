
"""
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

Nie jest poprawny, ponieważ w pythonie nie dajemy średników na końcu linii

"""
#poprawny kod:
x = 2
y = 3
if (x > y):
    result = x
else:
    result = y

print(result)

"""

for i in "axby": if ord(i) < 100: print (i)

Nie jest poprawny, ponieważ w pythonie wymagane są wcięcia, 
więc instrukcje if i print muszą być w nowych liniach lub trzeba zastosować
inną formę zapisu
"""
#poprawny kod:
for i in "axby":
    if ord(i) < 100:
        print (i)

for i in "axby": print(i) if ord(i) < 100 else None

"""

for i in "axby": print (ord(i) if ord(i) < 100 else i)

Poprawny

"""

for i in "axby": print (ord(i) if ord(i) < 100 else i)