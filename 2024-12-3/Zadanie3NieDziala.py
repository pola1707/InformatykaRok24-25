"""
KOD NIE DZIALA - UZYWAC Zadanie3Proba2.py
"""
fib = [0, 1]
a = 1
b = 1
c = 0
for i in range(38):
    c = a + b
    a = b
    b = c
    fib.append(c)

for j in range(len(fib)):
    fibBin = bin(fib[j])
    print(fibBin[2:])
