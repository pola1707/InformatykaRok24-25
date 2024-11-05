for i in range(10): #działa póki liczba nie będzie 9 (zaczyna od 0)
    print(i)   #wszystkie liczby w każdej nowej kolejce

for i in range(0, 10, 1): #dodaje co 1
    print(i, end=" ")  #wszystko po spacji

for j in range(1, 10, 2):  #dodaje co 2
    print(j, end=" ") #zmienna może byc co kolwiek

for _ in range(5): #zmienna może być wszystkim
    print("Środa") # nie trzeba wpisywać zmiennej w printa
print()

for element in range(10, -1, -1): # idzie w dół o 1 od 10 do 0
    print(element, end=" ")

