import sys


def find_indexes(word, letter):  # Funkcja do szukania indeksów podanej litery
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes


def state_of_game(no_of_tries, used_letters, user_word):
    print()
    print(" ".join(user_word))
    print("Pozostało prób: ", no_of_tries)
    print("Użyte litery: ", used_letters)
    print()


def level_choice():
    print()
    while True:
        level = input(
            "Wybierz stopień trudności: [1] - Łatwy [2] - Normalny [3] - Trudny: ")
        if level == "1":
            no_of_tries = 5
            break
        elif level == "2":
            no_of_tries = 3
            break
        elif level == "3":
            no_of_tries = 1
            break
        else:
            print("Błędna wartość")

    print("Liczba prób:", no_of_tries)
    print()
    return no_of_tries


def game(no_of_tries):

    used_letters = []  # Lista na użyte litery
    user_word = []  # Lista na litery

    for _ in word:  # Nigdzie nie korzystamy z żadnej zmiennej więc może być    podkreślenie
        # Wypełniamy listę pustymi znakami o długości zgadywanego słowa
        user_word.append("_")

    while True:
        letter = input("Podaj literę: ")
        used_letters.append(letter)

        # Indeksy podanych liter o ile są w słowie
        found_idexes = find_indexes(word, letter)

        if len(found_idexes) == 0:
            print("Nie ma takiej litery!")
            no_of_tries -= 1

            if no_of_tries == 0:
                print("Przegrałeś!")
                break
        else:
            for index in found_idexes:
                user_word[index] = letter

            if "".join(user_word) == word:
                print()
                print("Brawo, odgadłeś poprawne słowo!")
                break

        state_of_game(no_of_tries, used_letters, user_word)

    print("Twój wynik: ")
    state_of_game(no_of_tries, used_letters, user_word)

    used_letters.clear()
    user_word.clear()


word = "Natalia"  # Zgadywane słowo

while True:

    no_of_tries = level_choice()
    game(no_of_tries)

    play = input("Czy chcesz grać dalej? ")
    if play == "Tak":
        continue
    elif play == "Nie":
        print("Koniec gry!")
        sys.exit(0)
    else:
        print("Błędna wartość")
