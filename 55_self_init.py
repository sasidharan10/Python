class employee:

    # constructor (->none is mentioning the return type)

    def __init__(s, name, salary, role) -> None:
        s.name = name
        s.salary = salary
        s.role = role

    # self is taking the reference of the object

    def printdetails(s):
        print(
            f"The Name is {s.name} playing as {s.role} and salary is {s.salary}")
    pass


messi = employee("Messi", 2000, "Left Forward")
ronaldo = employee("Ronaldo", 1500, "Center Forward")

messi.printdetails()
ronaldo.printdetails()
