# Przypisuje do zmiennej wartosc podana z konsoli
light = input("Jakie jest światło (red, yellow, green)? ")

# Tutaj chyba nie trzeba nic tlumaczyc
if light == "red":
    print("Czekaj!")
elif light == "yellow":
    print("Przygotuj się!")
elif light == "green":
    print("Jedź!")
else:
    print("Niewłaściwa wartość!")

# Inny sposob, patrz 08-string.py
if str(light).startswith("r"):
    print("Czekaj!")
elif str(light).endswith("w"):
    print("Przygotuj się!")
elif light == "green":
    print("Jedź!")
else:
    print("Niewłaściwa wartość!")

# Jeszcze inny sposob wyswietlania warunkowego
print("Jedź!") if light == "green" else print("Czekaj!")
