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

    @classmethod
    def change_value(cls, val):
        cls.value = val

    @staticmethod
    def adding(a, b):
        return a+b


messi = employee("Messi", 20000, "Left Wing")
ronaldo = employee("Ronaldo", 15000, "Center Forward")

messi.printdetails()
print("\nValue (employee) :", employee.value)
messi.change_value(10)
ronaldo.change_value(15)
# or 
# messi.change_value=classmethod(messi.change_value)
# messi.change_value()
print("Value (messi) :", messi.value)
print("Value (ronaldo) :", ronaldo.value)
print("Value (employee) :", employee.value)

print("Add :", employee.adding(5, 6))
"""
- By using class method, we can modify class variables by using any instance variable.
- Instance methods are used to modify and access intance varibles.
- Static methods doesnt use class, instance variables. they are used for basic operations.
- no need to pass instance, variables to static methods

"""
