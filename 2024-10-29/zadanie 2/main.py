import random

def generate_random_string(length):
    random_string = ""
    for i in range(length):
        temp = random.randint(1, 3)
        match temp:
            case 1:
                 random_char = random.randint(ord('a'), ord('z'))
            case 2:
                random_char = random.randint(ord('A'), ord('Z'))
            case 3:
               random_char = random.randint(ord('0'), ord('9'))
        random_string += str(chr(random_char))
    return random_string+'.py'

current_file = "main.py"
with open(current_file, 'r') as file:
    code = file.read()
for i in range(10):
    copy_file = generate_random_string(8)
    with open(copy_file, "w") as file:
        file.write(code)