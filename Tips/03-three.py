# Typowe otwarcie i zamkniecie pliku
f = open("text.txt", "r")
file_contents = f.read()
f.close()

# Tip - otawrcie i zamkniecie pliku automatycznie
with open("text.txt", "r") as f:
    file_contents = f.read()
