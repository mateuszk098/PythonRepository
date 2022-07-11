# Ten program wyświetli nam informacje o cenie bitcoina w danej walucie pobierając informacje z zewnętrznego api CoinDesk

# Różnego rodzaju api mozemy znaleźć tutaj: https://github.com/public-apis/public-apis

import requests
import json

if __name__ == "__main__":
    # Kod który chcemy wyszukać (np. EUR, GBP, USD, PLN)
    code = input("Podaj kod: ")

    # Łączymy się z zewnętrznym api CoinDesk
    response = requests.get(
        f"https://api.coindesk.com/v1/bpi/currentprice/{code}.json")

    # Czy zapytanie się powiodło
    if response.status_code != requests.codes.ok:
        print("Coś poszło nie tak!")
    else:
        # Ładne wyświetlanie jsona, z wcięciem 4 znaków
        print(json.dumps(response.json(), indent=4))
