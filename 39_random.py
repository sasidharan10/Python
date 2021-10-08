import random
import math

print("\n-----Dice Game-----\n")
print("1) Roll Dice")
print("2) Quit")
ch = int(input("Enter Your Choice : "))
while(ch == 1):
    rn = random.randint(1, 6)
    print("Dice :", rn)
    ch = int(input("Press 1 to Roll Dice or 0 to Quit : "))

x = 56.93804

print("\nFloor :", math.floor(x))
print("Ceil :", math.ceil(x))
print("Trunc :", math.trunc(x))  # gives the no before the decimal
print("Sqrt :", math.sqrt(x))
print("PI :", math.pi)
print()
