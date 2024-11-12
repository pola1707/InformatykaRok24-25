def ostatniaCyfra(potega):
    if potega == 0:
        return 1
    cykl = [6, 2, 4, 8]
    return cykl[potega%4]
potega = int(input())
print(ostatniaCyfra(potega))