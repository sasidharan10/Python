class a:
    @staticmethod
    def showdata():
        print("\nThis is class A")

class b:
    @staticmethod
    def showdata():
        print("\nThis is class B")

class ab(a,b):

    # @staticmethod   # overriding occurs
    # def showdata():
    #     print("\nThis is class AB")

    pass

obj=ab()
obj.showdata()


"""
- when 2 base classes have methods with same name, the caling of method is based
  on the order of class from which it was derived. here class 'a' was inherited firt, so 
  method of a will execute.
"""