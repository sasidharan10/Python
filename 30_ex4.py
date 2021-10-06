n=int(input("Enter n : "))
c=int(input("Enter 0 or 1 : "))
i=0
j=0

if c==1:
    for i in range(n):
        for j in range(i):
            print("*",end="")
        print()
else:
    for i in reversed(range(n)):
        for j in range(i):
            print("*",end="")
        print()

