class Employee:
    def __init__(self,firstname,lastname,salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = int(salary)
    @staticmethod
    def from_string(string):
        name,surname,salary = [i for i in string.split("-")]
        return Employee(name,surname,salary)


