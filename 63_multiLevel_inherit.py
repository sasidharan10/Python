class grandfather():
    age = 50
    game = ["Basketball"]

    def printgame(obj):
        print("\nI Play :", end=" ")
        for i in obj.game:
            print(i, end=", ")


class father(grandfather):
    age = 30
    game = ["Basketball", "Cricket"]

    def printgame(obj):
        print("\nI Play :", end=" ")
        for i in obj.game:
            print(i, end=", ")


class son(father):
    age = 10
    game = ["Basketball", "Cricket", "Football"]

    def printgame(obj):
        print("\nI Play :", end=" ")
        for i in obj.game:
            print(i, end=", ")


larry = grandfather()
darry = father()
harry = son()

larry.printgame()
darry.printgame()
harry.printgame()
print("\nAge :", harry.age)


"""
- In inheritance, the compiler will first ook for a variable in the class for which
  the instance was created and then it will search for in the base class if not found.
  
"""
