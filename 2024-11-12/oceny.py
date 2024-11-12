#autor zadania: Mama Zdzisia
liczbaOcen = int(input())
oceny = input().split()
Jeden = 0
Dwa = 0
Trzy = 0
Cztery = 0
Piec = 0
Szesc = 0

for i in range(liczbaOcen):
    if oceny[i] == "1":
        Jeden += 1
    elif oceny[i] == "2":
        Dwa += 1
    elif oceny[i] == "3":
        Trzy += 1
    elif oceny[i] == "4":
        Cztery += 1
    elif oceny[i] == "5":
        Piec += 1
    elif oceny[i] == "6":
        Szesc += 1

print(f"{Jeden} {Dwa} {Trzy} {Cztery} {Piec} {Szesc}")