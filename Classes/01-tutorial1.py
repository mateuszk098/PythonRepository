# Classes and Instances

# Klasa pracownik
class Employee:

    # Konstruktor
    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@company.com"
        self.pay = pay

    # Metoda wyswietlajaca informacje o pracowniku
    def emp_info(self):
        print("\nFirst Name: " + self.first)
        print("Last Name: " + self.last)
        print("Email Address: " + self.email)
        print("Pay: " + str(self.pay))


# Main
if __name__ == "__main__":

    # Pracownicy
    emp_1 = Employee("Raven", "Bechtelar", 5000)
    emp_2 = Employee("Louie", "Feeney", 4000)

    # Wypisanie na ekran informacji o pracownikach
    Employee.emp_info(emp_1)
    Employee.emp_info(emp_2)
