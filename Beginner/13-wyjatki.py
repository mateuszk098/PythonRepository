# Tworzymy slownik krajow
countries_and_capitals = {"Poland": "Warsaw", "Germany": "Berlin"}

# Obsluga wyjatkow, w bloku try umieszczamy kod ktory moze spowodowac wyjatek
try:
    print(2 / 0)
    print(countries_and_capitals["USA"])
# W bloku except podajemy co ma sie stac jesli w try wystapi wyjatek
except KeyError:  # Wyjatek bledu klucza
    print("Klucz nie został znaleziony")
except ZeroDivisionError:  # Wyjatek dzielenie przez 0
    print("Nie można dzielić przez zero")
finally:
    print("To wykona się zawsze")

print("Jestem tutaj")
