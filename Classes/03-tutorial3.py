# Class methods and static methods

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

    # Class method, pozwala ustawiac zmienne klasowe
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Metoda rozdzielajaca string przechowujacy dane o pracowniku
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# Main
if __name__ == "__main__":

    # Pracownicy
    emp_1 = Employee("Raven", "Bechtelar", 5000)
    emp_2 = Employee("Louie", "Feeney", 4000)

    # Ustawienie zmiennej klasowej
    Employee.set_raise_amount = 1.05
    # print(emp_1.raise_amount)
    # print(emp_2.raise_amount)

    # Recznie
    emp_str_1 = "John-Doe-90000"
    first, last, pay = emp_str_1.split("-")
    new_emp_1 = Employee(first, last, pay)

    # Za pomoca metody klasowej
    emp_str_1 = "John-Doe-90000"
    new_emp_1 = Employee.from_string(emp_str_1)

    import datetime
    my_date = datetime.date(2021, 8, 31)
    print(Employee.is_workday(my_date))
