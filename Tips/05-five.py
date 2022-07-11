names = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heroes = ["Spiderman", "Superman", "Deadpool", "Batman"]
universes = ["Marvel", "DC", "Marvel", "DC"]

# Tip - mozemy wyswietlic wszystkie informacje stosujac zip
for name, hero, universe in zip(names, heroes, universes):
    print(name + " is actually " + hero + " from universe " + universe)

# Zip dziala jak tuple
for value in zip(names, heroes, universes):
    print(value)
