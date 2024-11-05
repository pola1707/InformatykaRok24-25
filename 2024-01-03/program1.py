'''
Program sprawdzający, która z dwóch liczb jest większa.

Przykład
Wejście:
1
3
Wyjście:
3
'''

number_1 = int(input())
number_2 = int(input())

if number_1 < number_2:
    print(number_2)
else:
    print(number_1)