class employee:
    value = 20   # class variable

    # constructor
    def __init__(self, name, salary, role) -> None:
        self.name = name
        self.salary = salary
        self.role = role

    # Instance method
    def printdetails(obj):
        print("Name :", obj.name)
        print("Salary :", obj.salary)
        print("Role :", obj.role)

    @staticmethod
    def adding(a, b):
        print("\nAdd :", a+b)


messi = employee("Messi", 20000, "Left Wing")
ronaldo = employee("Ronaldo", 15000, "Center Forward")

messi.printdetails()
messi.adding(5, 6)

"""
- Static methods doesnt use class, instance variables. they are used for basic operations.
- no need to pass instance, variables to static methods

"""