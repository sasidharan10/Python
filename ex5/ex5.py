def getdate():
    import datetime
    n = datetime.datetime.now()
    return n.strftime("Date = %d-%m-%Y, Time = %H:%M:%S")


print("\n----------Health Management System----------\n")
print("1) Update log")
print("2) Show log")
c = int(input("\nEnter your  choice : "))

if c == 1:
    print("\nClient List : \n")
    print("1) Rohan")
    print("2) Suraj")
    print("3) Raj")
    nm = int(input("Enter your choice : "))
    name = ""
    if nm == 1:
        name = "rohan"
    elif nm == 2:
        name = "suraj"
    else:
        name = "raj"
    print("\nUpdate %s's Food or Exercise : \n" % (name))
    print("1) Exercise")
    print("2) Food")
    d = int(input("\nEnter your  choice : "))
    if d == 1:
        f = open("{n}_ex.txt".format(n=name), "a")
        time = getdate()
        ex = input("Enter the exercise : ")
        f.write("{t} Exercise = {x}\n".format(t=time, x=ex))
        print("File Written Successfully!!!")
        f.close()
    else:
        f = open("{n}_f.txt".format(n=name),"a")
        time = getdate()
        fd = input("Enter the food : ")
        f.write("{t} Food = {x}\n".format(t=time, x=fd))
        print("File Written Successfully!!!")
        f.close()
else:
    print("\nClient List : \n")
    print("1) Rohan")
    print("2) Suraj")
    print("3) Raj")
    name = ""
    nm = int(input("Enter your choice : "))
    if nm == 1:
        name = "rohan"
    elif nm == 2:
        name = "suraj"
    else:
        name = "raj"

    print("\n%s's Food or Exercise : \n" % (name))
    print("1) Exercise")
    print("2) Food")
    d = int(input("\nEnter your choice : "))
    if d == 1:
        f = open("{n}_ex.txt".format(n=name), "rt")
        print("%s's Exercise Routine : " % (name))
        print(f.read())
        f.close()
    else:
        f = open("{n}_f.txt".format(n=name), "rt")
        print("%s's Food Routine : " % (name))
        print(f.read())
        f.close()
