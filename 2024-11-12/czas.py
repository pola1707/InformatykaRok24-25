sekundy = int(input())
godziny = 0
minuty = 0
reszta = 0
while sekundy >= 3600:
    godziny = sekundy // 3600
    reszta = sekundy % 3600
    sekundy = reszta


minuty = sekundy // 60
reszta = sekundy % 60
sekundy = reszta

print(f"{godziny}g{minuty}m{sekundy}s")