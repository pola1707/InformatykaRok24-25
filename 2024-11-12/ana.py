slowo = input().strip()
anagram = input().strip()

print(slowo)
if sorted(slowo) == sorted(anagram):
    print("TAK")
else:
    print("NIE")