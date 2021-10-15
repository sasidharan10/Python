class employee:
    def __init__(self,f,l) -> None:
        self.fname=f
        self.lname=l
        # self.email=f"\n{self.fname}.{self.lname}@gmail.com"

# """       
# setting email in constructor will not allow us to modify the 
# fname,lname in email string, as it will be initialised when the cnstructor
# called and cannot modify it again without calling the constructor
# """
    
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
fcb.fname="barcelona"
# fcb=employee("barcelona","Munich")

fcb.email="real.madrid@gmail.com"
print(fcb.email)

del fcb.email

print(fcb.email)
fcb.email="real.madrid@gmail.com"
print(fcb.email)



"""
- using "@property" will make the method to work as an attribute
- we can modify and delete the details in that methods by using setter and deleter
  which will work like an attribute(variable), makes it easy for the user to modify and
  delete it.

"""


