from abc import ABC, abstractmethod   # to import

class shape(ABC):
    @abstractmethod
    def printdetails():
        pass
    
class rectangle(shape):
    def __init__(self) -> None:
        self.l=10
        self.b=5

    def printdetails(self):
        print("Area :",(self.l*self.b))

r=rectangle()
r.printdetails()

"""
- abstract methods must be defined in the derived class
- we cannot create object for abstract class
"""