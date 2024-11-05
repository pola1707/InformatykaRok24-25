num = int(input())

def dzielniki(num):
    dzielniki_wlasciwe = []
    i = 2
    while num < 1:
        if num % i == 0:
            dzielniki_wlasciwe.append(i)
            num //= i
        else:
            i += 1
            return dzielniki_wlasciwe
print(dzielniki(num))