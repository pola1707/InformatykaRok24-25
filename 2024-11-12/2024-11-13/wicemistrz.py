"""
Autorzy kodu: Pola Brejt, Jan Krasiński

"""

druzyny = int(input())
punkty = input().split()

def najwiekszy(punkty):
    pozycjaNajwiekszej = 0
    najwieksza = 0
    for i in range(len(punkty)):
        i = int(i)
        punkty[i] = int(punkty[i])
        if punkty[i] > najwieksza:
            najwieksza = punkty[i]
            pozycjaNajwiekszej += 1
    return najwieksza



najwiekszyTemp = najwiekszy(punkty)
punkty.remove(najwiekszyTemp)
print(najwiekszy(punkty))
