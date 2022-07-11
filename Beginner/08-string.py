# Przypisanie wartosci do zmiennej
name = "mateusz"

# Zamiana pierwszej litery zmiennej string na wielką
print(name.capitalize())

# Zamiana całego stringa na wielkie litery
print(name.upper())

# Zamiana całego stringa na małe litery
print(name.lower())

# Pierwsza litera stringa
print(name[0])

# Litery zmiennej name od 1 do 3
print(name[1:3])

# Zmienna name od 3 litery
print(name[3:])

# Zmienna name do 2 litery
print(name[:2])

# Ostatnie 2 litery zmiennej name
print(name[-2:])

# Czy zmienna zaczyna się daną literą? Wielkość liter ma znaczenie
# Zwraca wartosc logiczna
print(name.startswith("m"))

# Czy zmienna konczy się daną literą? Wielkość liter ma znaczenie
# Zwraca wartosc logiczna
print(name.endswith("l"))

# Usuwa litere z prawej strony zmiennej
print(name.rstrip("z"))

# Usuwa litere z lewej strony zmiennej
print(name.lstrip("m"))

# Usuwa dana litere w zmiennej
print(name.strip("t"))

# Usuwa nadmierne spacje w zmiennej
print(name.strip())

# Przypisanie wartosci do zmiennej
channel = "Jak nauczyć się Pythona?"
# Rozdzielanie zmiennej channel na liste wyrazow wedlug spacji
print(channel.split(" "))

# Przypisanie wartosci do zmiennej
splitter = " "
# Polaczenie listy wyrazow splitterem
print(splitter.join(["Jak", "nauczyć", "się", "Pythona?"]))

# Przypisanie wartosci do zmiennych
first_name = "Mateusz"
last_name = "Kowalczyk"

# Wyswietla polaczone zmienne first_name i last_name ze spacja
print(first_name + " " + last_name)

# Wyswietla polaczone zmienne w liscie danym splitterem
print(splitter.join(["Mateusz", "Kowalczyk"]))

# Przypisanie wartosci do zmiennej
james_bond = 7
# Wyswietli 007 jako string
print(str(james_bond).zfill(3))
