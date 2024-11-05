money = 100
import random as rnd

bet = 5
while money > 0:
    computer_number = rnd.randint(1, 6)
    print(computer_number)
    user_number = int(input("Podaj liczbę od 1-6: "))
    if computer_number != user_number:
        money -= bet
    else:
        money += 2 * bet
    print(f'Saldo: {money}')
    key = input("Czy chcesz dalej grać? t/n: ")
    if key == "n":
        break

print("Miłego dnia!")