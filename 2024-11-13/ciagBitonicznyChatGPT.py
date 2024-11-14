def czyBitoniczny(liczbaArg, bitoniczny):
    if liczbaArg == 1:
        return "TAK"
    i = 0
    while i < liczbaArg - 1 and bitoniczny[i] < bitoniczny[i + 1]:
        i += 1
    while i < liczbaArg - 1 and bitoniczny[i] > bitoniczny[i + 1]:
        i += 1
    return "TAK" if i == liczbaArg - 1 else "NIE"
liczbaArg = int(input())
bitoniczny = list(map(int, input().split()))
print(czyBitoniczny(liczbaArg, bitoniczny))