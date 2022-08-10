import datetime
import random

letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
           'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z')
symbols = ('@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<')


def append_to_log(log_string):
    password_log = open("password_log.txt", "a")
    password_log.write(log_string + "\t" + str(datetime.datetime.today()) + "\n")
    password_log.close()


print("Menu Option: ")
print("\tPress 1 to Generate new password")
print("\tPress 2 to View recently generated password")

is_option_valid = False
while not is_option_valid:
    try:
        option = int(input("Please enter 1 or 2: "))
        if option < 0 or option > 2:
            raise Exception("Option must be either 1 or 2. Please enter again!")
        is_option_valid = True
    except ValueError:
        print("Only digits are allowed! Please enter again!")
        is_option_valid = False
    except:
        is_option_valid = False

if option == 1:
    is_password_length_valid = False
    while not is_password_length_valid:
        try:
            password_length = int(input("Password Length: "))
            if password_length < 4:
                raise Exception("Password length must be greater than 3. Please enter again!")
            is_password_length_valid = True
        except ValueError:
            print("Only digits are allowed! Please enter again!")
            is_password_length_valid = False
        except:
            is_password_length_valid = False

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
    append_to_log(password)

elif option == 2:
    try:
        password_log = open("password_log.txt", "r")
    except FileNotFoundError:
        print("You have not generated any passwords yet. Try create one!")

    print("Password \t Created on")
    for password in password_log.readlines():
        print(password)
    password_log.close()







