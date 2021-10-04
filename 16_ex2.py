print("\n----------CALCULATOR----------\n")
print("1) Addition")
print("2) Subtraction")
print("3) Multiplication")
print("4) Division")
x = int(input("Enter A : "))
y = int(input("Enter B : "))
c = int(input("Enter Your Operation : "))

if c == 1:
    if x == 56 and y == 9:
        ans = 77
    else:
        ans = x+y
elif c == 2:
    ans = x-y
elif c == 3:
    if x == 45 and y == 3:
        ans = 555
    else:
        ans = x*y
elif c == 4:
    if x == 56 and y == 6:
        ans = 4
    else:
        ans = x/y
else:
    print("Invalid Input!!!")

print("Answer :", ans)
