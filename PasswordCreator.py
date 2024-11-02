import random as rnd

lenght = rnd.randint(12, 25)
Password = ""

Password += str(chr(rnd.randint(ord("a"), ord("z"))))
Password += str(chr(rnd.randint(ord("A"), ord("Z"))))
Password += str(chr(rnd.randint(ord("0"), ord("9"))))
Password += str(chr(rnd.randint(ord("!"), ord("/"))))
Password += str(chr(rnd.randint(ord(":"), ord("@"))))
Password += str(chr(rnd.randint(ord("["), ord("`"))))
Password += str(chr(rnd.randint(ord("{"), ord("~"))))

for i in range(lenght - 7):
    temp = rnd.randint(1, 6)
    match temp:
        case 1:
            random_char = rnd.randint(ord("a"), ord("z"))
        case 2:
            random_char = rnd.randint(ord("A"), ord("Z"))
        case 3:
            random_char = rnd.randint(ord("0"), ord("9"))
        case 4:
            random_char = rnd.randint(ord("!"), ord("/"))
        case 5:
            random_char = rnd.randint(ord(":"), ord("@"))
        case 5:
            random_char = rnd.randint(ord("["), ord("`"))
        case 6:
            random_char = rnd.randint(ord("{"), ord("~"))
    Password += str(chr(random_char))

print(Password)
