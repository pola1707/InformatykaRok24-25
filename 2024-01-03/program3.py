a, b = map(float, input().split())

if a != 0:
    x = -b/a
    print(f"x = {x:0.2f}")
elif b == 0:
    print(f"Nieskończenie wiele rozwiązań")
else:
    print("Brak rozwiązań")
