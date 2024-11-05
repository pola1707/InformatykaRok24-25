import random
import random as rnd

computer_random_number = random.randint (1, 100)
print(computer_random_number)
user_number = 0

counter = 0
while computer_random_number != user_number:
    user_number = int(input("Podaj liczbę: "))
    if computer_random_number < user_number:
        print("Za dużo")
    if computer_random_number > user_number:
         print("Za mało")
    counter += 1
print(f"Koniec gry po {counter} próbach")


