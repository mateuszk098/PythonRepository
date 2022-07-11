# Przyglądamy się bibliotece requests i łączymy z zewnętrznym API z poziomu aplikacji

# Importujemy bibliotekę requests
import requests

if __name__ == "__main__":

    # Zapytanie get
    response = requests.get("http://jsonplaceholder.typicode.com/posts/1")

    # Czy zapytanie się powiodło
    if response.status_code != requests.codes.ok:
        print("Coś poszło nie tak!")
    else:
        print(response.json())

    requests_body = {
        "title": "Nasz tytuł",
        "body": "Treść posta",
        "userId": 1
    }

    response = requests.post(
        "http://jsonplaceholder.typicode.com/posts", json=requests_body)

    # Czy zapytanie się powiodło
    if response.status_code != requests.codes.created:
        print("Coś poszło nie tak!")
    else:
        print(response.json())
