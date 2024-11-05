numbers = []

for i in range (10):
    number = input(f"Podaj {i}-tą liczbę: ")
    numbers.append(number)

print(numbers)
numbers = list(map(int, numbers))
print(numbers)

search_number = int(input("Podaj liczbę szukaną: "))

for x in numbers:
    if x == search_number:
        print("Znalazłem")

for i in range(len(numbers)):
    if search_number == numbers[i]:
        print("znalazłem")
