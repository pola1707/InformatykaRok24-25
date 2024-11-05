lista_slow = []
lista_slow_nieparzystych = []
for _ in range(7):
    word = input()
    if len(word) % 2 == 0: lista_slow.append(word)
    else: lista_slow_nieparzystych.append(word[::-1])
for w in lista_slow_nieparzystych: lista_slow.append(w)
print(*lista_slow)