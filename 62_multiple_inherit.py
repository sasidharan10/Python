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

class player:   # inheritance
    value=10
    
    def __init__(self, name, game) -> None:
        
        self.name=name
        self.game=game
        
class coolProgrammer(employee,player):

    def __init__(self, name, salary, role,mng) -> None:
        super().__init__(name, salary, role)   # calling base constructor
        self.mng=mng

    def printcnt(self):
        print("\nName :", self.name)
        print("Salary :", self.salary)
        print("Role :", self.role)
        print("Manager :",self.mng)

messi = employee("Messi", 20000, "Left Wing")
ronaldo = employee("Ronaldo", 15000, "Center Forward")
neymar= coolProgrammer("Neymar", 18500, "Right Wing","Pochetino")

messi.printdetails()
neymar.printdetails()
print("Value :",neymar.value)
neymar.printcnt()

"""
- when we try to access a variable which is present in both base classes, then
  the compiler will access the variable from the first base class by default.
- The derived class from  2 base class will call the first constructor by default.

"""
