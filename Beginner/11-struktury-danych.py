# LISTY
# W listach mozemy miec zmienne roznego typu, jednakze najczesciej
# jest to jeden typ zmiennej

# Tworzymy pusta liste
names_list1 = []
# Dodajemy dana wartosc na koncu listy
names_list1.append("Mateusz")
# Dodajemy dana wartosc na koncu listy
names_list1.append("Mariusz")
# Wyswietlamy liste
print(names_list1)

# Tworzymy druga liste
names_list2 = ["Dominik"]

# Laczymy dwie listy
names_list = names_list1 + names_list2

# Tworzymy liste ze zmiennymi
names = ["Kamil", "Mariusz", "Adam", "Kamil"]
# Wyswietlamy liste
print(names)

# Wyswietlamy wartosci w liscie
for name in names:
    print(name)

# Odwrocenie kolejnosci w liscie
names.reverse()

# Sortuje alfabetycznie liste
names.sort()

# Sortuje alfabetycznie i odwraca kolejność
names.sort(reverse=True)

# Pierwszy element listy
names[0]

# Zlicza ilość wystąpień danej zmiennej
names.count("Kamil")

# Podaje długość listy
len(names)

# Usuwa element o indeksie 0 z listy
names.pop(0)

# Usuwa duplikaty w liscie
names.remove("Kamil")

# Czyści listę
names.clear()


# TUPLE
# Tuple jest niezmienna, w momencie stworzenia tuple'a nie możemy nic do niej dodać, usunąć, etc.. Jej dobrym zastosowaniem jest przechowywanie różnych informacji różngo typu

# Tworzymy tuple'a
person = ("Mateusz", "Kowalczyk", 23)

# Wyswietlamy tuple'a
print(person)

# Wyswietlamy ilosc zliczen zmiennej
print(person.count("Mateusz"))


# SET
# Set jest podobny do listy ale w secie nie można mieć zduplikowanych danych, elementy seta sa posortowane

# Tworzymy set
names_set1 = {"Mateusz", "Mariusz", "Mateusz"}

# Wyswietlamy set, wyswietli tylko oryginale zmienne, duplikaty usunie
print(names_set1)

# Tworzymy pusty set
set_null = set()

# Dodajemy wartosc do setu
set_null.add("Mateusz")

# Wyswietlamy set
print(set_null)

# Tworzymy drugi set
names_set2 = {"Dominik"}

# Tworzymy trzeci set, ktory jest polaczeniem 1 i 2
names_set3 = names_set1.union(names_set2)

# Zaktualizowanie setu 2 o set 3
names_set2.update(names_set3)

# Różnica setów, z setu 1 usuwa elementy ktore znalazl w 2 secie (jesli znalazl te same)
names_set4 = names_set1.difference(names_set2)

# Czesc wspolna setow 1 i 2
names_set4 = names_set1.intersection(names_set2)

# Nie cześć wspolna setow 1 i 2
names_set4 = names_set1.symmetric_difference(names_set2)

# Tworzymy liste i set
person_list = ["Mateusz", "Mariusz"]
person_set = {"Dominik"}

# Rozszerzenie listy o set
person_list.extend(person_set)


# SŁOWNIK
# Slownik to struktura danych typu klucz - wartosc, w slowniku
# nie można miec dwoch tych samych kluczy

# Tworzymy slownik z krajami i ich stolicami
countries_and_capitals = {"Poland": "Warsaw", "Germany": "Berlin"}

# Dodanie nowej zmiennej do slownika, podajemy klucz "Italy" pod ktorym
# chcemy przechowac wartosc "Rome"
countries_and_capitals["Italy"] = "Rome"

# Wyswietlamy slownik
print(countries_and_capitals)

# Wyswietlamy klucze slownika, w tym przypadku sa to nazwy krajow
for country in countries_and_capitals.keys():
    print(country)

# Wyswietlamy wartosci slownika, w tym przypadku sa to nazwy stolic
for capital in countries_and_capitals.values():
    print(capital)

# Wyswietlamy zarowno klucze jak i wartosci slownika
for country, capital in countries_and_capitals.items():
    print(country + "-" + capital)

# Wyswietlamy wartosc klucza, jesli klucz nie istnieje to mamy error
print(countries_and_capitals["Poland"])

# Wyswietlamy wartosc klucza, jesli klucz nie istnieje to zwroci None
print(countries_and_capitals.get("Poland"))

# setdefault pobiera wartosc z danego klucza, jesli klucza nie ma
# to dodaje ten klucz wraz z wartoscia
print(countries_and_capitals.setdefault("USA", "Washington DC"))

# Usuwa wartosc znajdujaca sie pod danym kluczem
countries_and_capitals.pop("Poland")

# Usuwa ostatnio dodany element
countries_and_capitals.popitem()

# Czy znaleziono zmienna jako klucz w slowniku
if "Poland" in countries_and_capitals.keys():
    print("Znaleziono")
else:
    print("Nie znaleziono")

# Czyszczenie słownika
countries_and_capitals.clear()
