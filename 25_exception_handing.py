a = input("Enter A : ")
b = input("Enter B : ")

try:
    print("\nSum :", int(a)+int(b))
except Exception as f:
    print("\nInvalid input :", f)

print("\nProgram is over :)")
