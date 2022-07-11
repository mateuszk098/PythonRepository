names = ["Corey", "David", "Chris", "Travis"]

# Normalne wyswietlenie z indexami
index = 0
for name in names:
    print(index, name)
    index += 1

# Tip - zastosowanie enumerate
for index, name in enumerate(names):
    print(index, name)
