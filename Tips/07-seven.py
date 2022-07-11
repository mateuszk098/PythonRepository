# Klasy, metody getarr i setarr
class Person:
    pass


person = Person()
person_info = {"first": "Corey", "last": "Schafer"}

# Ustawiamy atrybuty
for key, value in person_info.items():
    setattr(person, key, value)

# Czytamy atrybuty
for key, value in person_info.items():
    print(getattr(person, key, value))
