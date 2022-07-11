# Property decorators

# Klasa pracownik
class Employee:

    # Konstruktor
    def __init__(self, first: str, last: str):
        self.first = first
        self.last = last

    @property
    def email(self):
        return self.first + "." + self.last + "@company.com"

    @property
    def fullname(self):
        return self.first + " " + self.last

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete name!")
        self.first = None
        self.last = None


# Main
if __name__ == "__main__":

    emp_1 = Employee("Ruben", "Cummings")
    emp_1.first = "Jim"

    print(emp_1.first)
    print(emp_1.email)
    print(emp_1.fullname)

    emp_1.fullname = "Corey Schafer"

    print(emp_1.first)
    print(emp_1.email)
    print(emp_1.fullname)

    del emp_1.fullname
