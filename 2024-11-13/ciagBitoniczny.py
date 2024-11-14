"""Nieudana próba tego zadania"""
liczbaArg = int(input())
ciagBitoniczny = list(map(int, input().split()))
najwiekszaTemp = 0
iterator = 1
iteratorDwa = 1
def najwiekszy(ciagBitoniczny):
    pozycjaNajwiekszej = 0
    najwieksza = 0
    for i in range(len(ciagBitoniczny)):
        i = int(i)
        ciagBitoniczny[i] = int(ciagBitoniczny[i])
        if ciagBitoniczny[i] > najwieksza:
            najwieksza = ciagBitoniczny[i]
            pozycjaNajwiekszej += 1
    return pozycjaNajwiekszej

pozycjaSrodku = najwiekszy(ciagBitoniczny)

if pozycjaSrodku == 0 or pozycjaSrodku == 1:
    print("NIE")
najmniejszaTemp = pozycjaSrodku + 1

for i in range(pozycjaSrodku):
    if ciagBitoniczny[i] > najwiekszaTemp:
        najwiekszaTemp = ciagBitoniczny[i]
        iterator += 1
    else:
        print("NIE")
        break

if iterator == pozycjaSrodku:
    for j in range(pozycjaSrodku, len(ciagBitoniczny)):
        if ciagBitoniczny[pozycjaSrodku + j] < najmniejszaTemp:
            najmniejszaTemp = ciagBitoniczny[pozycjaSrodku + j]
            iteratorDwa += 1
        else:
            print("NIE")
            break

if iterator == pozycjaSrodku and iteratorDwa == (len(ciagBitoniczny) - pozycjaSrodku):
    print("TAK")

