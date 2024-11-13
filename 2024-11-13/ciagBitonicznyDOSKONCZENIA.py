#DO DOKONCZENIA - kod nie zwraca TAK, jesli kod ma na 1 miejscu i jest git to zla odp
liczbaArg = int(input())
ciagBitoniczny = list(map(int, input().split()))
najwiekszaTemp = 0
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


for i in range(pozycjaSrodku):
    if pozycjaSrodku == 0 or pozycjaSrodku == 1:
        print("NIE")
        break
    elif ciagBitoniczny[i] > najwiekszaTemp:
        najwiekszaTemp = ciagBitoniczny[i]
        break
    else:
        print("NIE")
        break
