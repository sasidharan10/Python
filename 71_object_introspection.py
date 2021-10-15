import inspect

class employee:
    def __init__(self,f,l) -> None:
        self.fname=f
        self.lname=l
    
    def detail(self):
        print("\nFirst name :",self.fname)
        print("Last name :",self.lname)
    
    @property
    def email(self):
        if self.fname==None or self.fname==None:
            print("Email IS not Set!!!")
        else:
            return f"\n{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self,i):
        ls=i.split('@')[0]
        self.fname=ls.split('.')[0]
        self.lname=ls.split('.')[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None

fcb=employee("Bayern","Munich")
fcb.detail()
print(fcb.email)
print("Typr :",type(fcb))
print("ID :",id(fcb))
print("\nDir :",dir(fcb))  # return all methods and attributes of given object
import math
print("\nDir of math:",dir(math))

print("\nGetmembers :",inspect.getmembers(fcb)) # return all memebers in (name,value) pairs

