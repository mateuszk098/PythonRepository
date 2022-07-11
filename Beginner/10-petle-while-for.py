# Przypisanie wartosci do zmiennej
number = 1

# Dopoki number < 6 to wyswietlaj i inkrementuj number o 1
while number < 6:
    print(number)
    number += 1

# Wieswietl liczby co 2 z zakresu 0-9
for number in range(0, 10, 2):
    print(number)

# Wyswietlaj liczby z zakresu 0-9, jesli natrafi na 5 to przerwij
for number in range(0, 10):
    if number == 5:
        break
    print(number)

# Wyswietlaj liczby z zakresu 0-9, jesli natrafi na 5 to przerwij aktualne
# wykonanie i przejdz do kolejnej iteracji
for number in range(0, 10):
    if number == 5:
        continue
    print(number)
