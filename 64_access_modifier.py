class football:
    networth = 10000        # Public
    _salary = 100           # Protected
    __blackmoney = 1000     # Private

    def printdetails(self):
        print("\nNetworth (using public method) :", self.networth)
        print("Salary (using public method) :", self._salary)
        print("Blackmoney (using public method) :", self.__blackmoney)


class premier(football):
    # protected variable can be accessed by derived class
    sal = football._salary
    # blk=football.__blackmoney     # private cannot getting accessed by derived class
    pass


f = premier()
print("\nNetworth (Outside) :", f.networth)
print("Salary (Outside) :", f._salary)
# print("Blackmoney :",f.__blackmoney)  # we cannot access private varaible as it is

f.printdetails()

print("\nBlackmoney (Name Mangling) :", f._football__blackmoney)

"""
- We can access private members either by using a public method or
  we can directly access them by "name mangling"
  
"""
