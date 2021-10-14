class base:
    num=10
    str="Hello"

    def __init__(self) -> None:
        self.num=40
        print("\nBase Constructor Called")

class derived(base):
    num=20   # class variable
    str="Good Morning"

    def __init__(self) -> None:
        print("\nDerived Constructor Called")
        self.num=30   # instance variable
        super().__init__()  # derived constructor gets overriden by base constructor 

# b=base()
d=derived()
print("Num :",d.num)

"""
- In a single inheritance, whenever we want to access a variable, the compiler will
  first check for its instance variable in the given class, and then it will look
  for it in the base class for the instance variable.
- Instance variable has high priority than class variable.
- Always the derived constructor get called as it overrides the base constructor, so
  the base cnstructor never gets called. In order to callled the base constructor, 
  we have to use super()__init__() to call the base constructor.

"""