# Class variables

# Klasa pracownik
class Employee:

    # Tworzymy zmienna klasowa, procent o jaki zwiekszamy pay
    raise_amount = 1.05
    # Zmienna klasowa, liczba pracownikow
    num_of_emps = 0

    # Konstruktor
    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@company.com"
        self.pay = pay

        # Za kazdym razem kiedy tworzymy obiekt pracownik w main, ta zmienna sie inkrementuje
        Employee.num_of_emps += 1

    # Metoda wyswietlajaca informacje o pracowniku
    def emp_info(self):
        print("\nFirst Name: " + self.first)
        print("Last Name: " + self.last)
        print("Email Address: " + self.email)
        print("Pay: " + str(self.pay))

    # Metoda modyfikujaca kwote o dany procent
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# Main
if __name__ == "__main__":

    # Pracownicy
    emp_1 = Employee("Raven", "Bechtelar", 5000)
    emp_2 = Employee("Louie", "Feeney", 4000)

    # Liczba pracownikow
    print("Employees: " + str(Employee.num_of_emps))

    # Wypisanie na ekran informacji o pracownikach
    Employee.emp_info(emp_1)
    Employee.emp_info(emp_2)

    # Modyfikujemy pay pracownika emp_1 i wypisujemy info
    Employee.apply_raise(emp_1)
    Employee.emp_info(emp_1)

    # Modyfikujemy raise_amount dla pracownika emp_1
    emp_1.raise_amount = 1.10
    # Modyfikujemy pay pracownika emp_1 i wypisujemy info
    Employee.apply_raise(emp_1)
    Employee.emp_info(emp_1)
    # raise_amount dla pracownika emp_2 jest taki sam jak wczesniej
    Employee.apply_raise(emp_2)
    Employee.emp_info(emp_2)
