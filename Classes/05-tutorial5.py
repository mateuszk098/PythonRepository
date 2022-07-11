# Special methods

# Klasa pracownik
class Employee:

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

    # Both str() and repr() methods in python are used for string representation of a string.
    # The __str__ is used to find the “informal”(readable) string representation of an object whereas __repr__ is used to find the “official” string representation of an obj
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.emp_info(), self.email)

    # Add salaries of eployees
    def __add__(self, other):
        return self.pay + other.pay


# Main
if __name__ == "__main__":

    emp_1 = Employee("Ruben", "Cummings", 50000)
    emp_2 = Employee("Rico", "Durgan", 60000)

    print(repr(emp_1))
    print(str(emp_1))
    print(emp_1+emp_2)
