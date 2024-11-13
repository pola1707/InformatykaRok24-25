"""
Autorzy: Jan Krasiński, Pola Brejt

"""

dni, szukana = input().split()
akcje = input().split()
akcjePoz = []
akcjePozBezCyfry = ["-1", "-1"]

for i in range(int(dni)):
    if akcje[i] == szukana:
        akcjePoz.append(i + 1)

if akcjePoz == []:
    print(*akcjePozBezCyfry)
else:
    print(akcjePoz[0], akcjePoz[len(akcjePoz) - 1])