import random

letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
           'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z')
symbols = ('@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<')
isPasswordLengthValid = False

while not isPasswordLengthValid:
    try:
        password_length = int(input("Password Length: "))
        isPasswordLengthValid = True
    except ValueError:
        print("Only digits are allowed! Please enter again!")
        isPasswordLengthValid = False

# Strong Password must-have: letters, digits, symbols

random_number = random.randint(0, len(letters) - 1)
password = letters[random_number]
random_number = random.randint(0, 9)
password += str(random_number)
random_number = random.randint(0, len(symbols) - 1)
password += symbols[random_number]

for i in range(4, password_length + 1):
    random_number = random.randint(1, 10000)

    # uppercase letter
    if random_number % 4 == 0:
        password += letters[random.randint(0, len(letters) - 1)].upper()
    # lowercase letter
    elif random_number % 4 == 1:
        password += letters[random.randint(0, len(letters) - 1)]
    # digits
    elif random_number % 4 == 2:
        password += str(random.randint(0, 9))
    # symbols
    elif random_number % 4 == 3:
        password += symbols[random.randint(0, len(symbols) - 1)]

print("Your generated password: " + password)



