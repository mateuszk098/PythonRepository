# Otwiera plik do zapisu i odczytu
file = open("countries_and_capitals.txt", "w+")

# Tworzymy slownik kraje + stolice
countries_and_capitals = {"Poland": "Warsaw", "Germany": "Berlin"}

# Dla kluczy i ich wartosci, zapisz te zmienne do pliku
for country, capital in countries_and_capitals.items():
    file.write(country + "-" + capital + "\n")

# Zamyka plik
file.close()

# Otwieramy plik
file = open("countries_and_capitals.txt")
# Dla kazdej linii w pliku, wyswietl te linie
for line in file.readlines():
    print(line.strip())

# Zamyka plik
file.close()
