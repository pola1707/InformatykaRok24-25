a, b = map(int, input("Podaj dwie liczby: ").split())

print(a,b)

while a != b:
    if a > b:
        a -= b
    else:
        b -= a

print(a)