import datetime

class car:
    def __init__(self,name,speed,mileage) -> None:
        self.name=name
        self.speed=speed
        self.mileage=mileage

    def __add__(self,other):
        return self.speed+other.speed
    
    def __sub__(self,other):
        return self.speed-other.speed

    def __mul__(self,other):
        return self.speed*other.speed
    
    def __truediv__(self,other):
        return self.speed/other.speed

    def __repr__(self) -> str:
        return f"__repr__\nName : {self.name}\nSpeed : {self.speed}\nMileage : {self.mileage}\n"

    # def __str__(self) -> str:
    #     return f"__str__\nName : {self.name}\nSpeed : {self.speed}\nMileage : {self.mileage}\n"

tesla=car("model S",250,150)
bmw=car("X7",180,20)

print(tesla)
# operator overlloading
print("Speed Add :",tesla+bmw)
print("Speed Dif :",tesla-bmw)
print("Speed Mul :",tesla*bmw)
print("Speed Div :",tesla/bmw)

"""
- repr and str are used for printing string representation of the object. str overwrites repr 
  and repr gets printed if str not exists.
"""