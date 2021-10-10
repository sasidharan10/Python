class student:
    seat = 20
    pass


rohan = student()
mohan = student()

rohan.name = "rohan"
rohan.std = 12
rohan.seat = 15

mohan.name = "mohan"
mohan.std = 11
mohan.seat = 23

print("rohan seat : ", rohan.seat)
print("mohan seat : ", mohan.seat)
print("student seat : ", student.seat)

"""

- seat is a class variable which can be changed only by using class name
- when we access to change it with rohan or mon=han object, we basically making a
  instance of that variable in both objects.
  
"""
