# Tworzymy slownik z krajami i ich stolicami oraz liczba mieszkancow
countries_information = {}
countries_information["Polska"] = ("Warszawa", 37.97)
countries_information["Niemcy"] = ("Berlin", 83.02)
countries_information["Słowacja"] = ("Bratysława", 5.45)


# Funkcja ktora wyswietli nam informacje o podanym kraju
def show_country_info(country: dict):

    # Przypisujemy wartosc kluczy do nowej listy
    coutry_information = countries_information.get(country)

    # Wyswietlamy nazwe kraju
    print()
    print(country)

    # Wyswietlamy informacje o podanym kraju
    print("-------")
    print("Stolica: " + coutry_information[0])
    print("Liczba mieszkańców (mln): " + str(coutry_information[1]))


if __name__ == "__main__":

    # Wysweitlamy nazwy krajow w slowniku
    for country in countries_information.keys():
        print(country)

    # Podajemy z konsoli o jakim kraju chcemy inforamcje
    country = input("Informacje o jakim kraju chcesz wyśietlić? ")

    # Wywolujemy funkcje dla teog kraju
    show_country_info(country)
