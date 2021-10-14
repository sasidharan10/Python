class employee:
    value = 20   # class variable

    # constructor
    def __init__(self, name, salary, role) -> None:
        self.name = name
        self.salary = salary
        self.role = role

    # Instance method
    def printdetails(obj):
        print("\nName :", obj.name)
        print("Salary :", obj.salary)
        print("Role :", obj.role)


class manager(employee):
    networth = 1000

    def __init__(self, name, salary, role, mng) -> None:
        super().__init__(name, salary, role)
        self.mng = mng

    def printmng(obj):
        obj.printdetails()
        print("Manager :", obj.mng)


messi = employee("Messi", 20000, "Left Wing")
ronaldo = employee("Ronaldo", 15000, "Center Forward")
neymar = manager("Neymar", 18500, "Right Wing", "Pochetino")

messi.printdetails()
neymar.printmng()
