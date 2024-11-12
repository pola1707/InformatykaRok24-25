#DO POPRAWY

druzyny = int(input())
najwieksza = 0
punkty = input().split()

def najwiekszy(punkty):
    pozycjaNajwiekszej = 0
    for i in punkty:
        if punkty[i] > najwieksza:
            najwieksza = punkty[i]
        pozycjaNajwiekszej += 1

print(najwiekszy(punkty))

