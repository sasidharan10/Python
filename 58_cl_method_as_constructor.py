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
        print()

    @classmethod
    def from_str(cls, str):
        ls = str.split("-")
        return cls(ls[0], ls[1], ls[2])


messi = employee("Messi", 20000, "Left Wing")
ronaldo = employee("Ronaldo", 15000, "Center Forward")
neymar = employee.from_str("Neymar-18500-Forward")

messi.printdetails()
neymar.printdetails()
