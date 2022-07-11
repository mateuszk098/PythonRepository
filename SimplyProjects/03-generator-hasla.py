import sys
import random
import string

password = []
character_left = 0


def update_character_left(number_of_character):

    global character_left

    if number_of_character < 0 or number_of_character > character_left:
        print("Liczba znaków przekracza zakres")
        sys.exit(0)
    else:
        character_left -= number_of_character
        print("Pozostało znaków: ", character_left)


password_length = int(input("Jak długie ma być hasło? "))

if password_length < 5:
    print("Hasło nie może być krótsze niż 5 znaków. Spróbuj ponownie.")
    sys.exit(0)
else:
    character_left = password_length

lowercase_letter = int(input("Ile małych liter ma mieć hasło? "))
update_character_left(lowercase_letter)

uppercase_letter = int(input("Ile dużych liter ma mieć hasło? "))
update_character_left(uppercase_letter)

special_character = int(input("Ile znaków specjalnych ma mieć hasło? "))
update_character_left(special_character)

digits = int(input("Ile cyfr ma mieć hasło? "))
update_character_left(digits)

if character_left > 0:
    print("Nie wszystkie znaki zostały wykorzystane. Hasło zostanie uzupełnione małymi literami.")
    lowercase_letter += character_left

print()
print("Małe litery: ", lowercase_letter)
print("Duże litery: ", uppercase_letter)
print("Znaki specjalne: ", special_character)
print("Cyfry: ", digits)

for _ in range(password_length):
    if lowercase_letter > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letter -= 1
    if uppercase_letter > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letter -= 1
    if special_character > 0:
        password.append(random.choice(string.punctuation))
        uppercase_letter -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)
print("Hasło: ", "".join(password))

# Można szybciej :)

password_fast = "".join(random.choice(string.ascii_uppercase +
                        string.ascii_lowercase + string.punctuation + string.digits) for _ in range(password_length))
print("Szybkie hasło: ", password_fast)
