# Subclasses

# Klasa pracownik
class Employee:

    # Tworzymy zmienna klasowa, procent o jaki zwiekszamy pay
    raise_amount = 1.05

    # Konstruktor
    def __init__(self, first: str, last: str, pay: int):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@company.com"
        self.pay = pay

    # Metoda wyswietlajaca informacje o pracowniku
    def emp_info(self):
        return self.first + " " + self.last

    # Metoda modyfikujaca kwote o dany procent
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):

    raise_amount = 1.10

    def __init__(self, first: str, last: str, pay: int, prog_lang: str):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    raise_amount = 1.10

    def __init__(self, first: str, last: str, pay: int, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.emp_info())


# Main
if __name__ == "__main__":

    # Pracownicy
    dev_1 = Developer("Raven", "Bechtelar", 5000, "Python")
    dev_2 = Developer("Louie", "Feeney", 4000, "Java")

    print(dev_1.email)
    print(dev_1.prog_lang)

    # Managerowie
    mag_1 = Manager("Sue", "Smith", 9000, [dev_1])
    mag_1.print_emps()

    mag_1.add_emp(dev_2)
    mag_1.print_emps()
