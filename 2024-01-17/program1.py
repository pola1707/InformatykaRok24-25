age = int(input())

if age < 18:
    print("szczeniastwo, nie dotykać")
else:
    print("osoba pełnoletnia")

if age < 18:
    print("szczeniastwo, nie dotykać")
else:
    if age < 85:
        print("osoba pełnoletnia")
    else:
        print("senior")

if age < 18:
    print("niepełnoletni")
elif age < 85:
    print("pełnoletni")
else:
    print("senior")


# < mniejsze, <= mniejszerówne, > większe, >= większerówne
'''
a = 2     równa się
a == 2    porównanie
'''