from tkinter import *


def getvals():
    print("Name :", namevalue.get())
    print("Age :", agevalue.get())
    print("Contact :", contactvalue.get())
    print("City :", cityvalue.get())
    print("Coupon :", couponvalue.get())

    with open("data.txt","a") as t:
        t.write(f"Name : {namevalue.get()}\nAge : {agevalue.get()}\nContact : {contactvalue.get()}\nCity : {cityvalue.get()}\nCoupon : {couponvalue.get()}\n")



root = Tk()
root.geometry("600x400")
root.title("Happy Travels")

# heading
Label(root, text="Welcome To Happy Travels", font="arial 15 bold").grid(
    row=0, pady=10, padx=10)

# labels

Label(root, text="Name : ",).grid(row=1, pady=5)
Label(root, text="Age : ",).grid(row=2, pady=5)
Label(root, text="Contact : ",).grid(row=3, pady=5)
Label(root, text="City : ",).grid(row=4, pady=5)
# Label(text="Want Coupon ? : ",).grid(row=5)

namevalue = StringVar()
agevalue = StringVar()
contactvalue = StringVar()
cityvalue = StringVar()
couponvalue = IntVar()

Entry(root, textvariable=namevalue,).grid(row=1, column=2)
Entry(root, textvariable=agevalue).grid(row=2, column=2)
Entry(root, textvariable=contactvalue).grid(row=3, column=2)
Entry(root, textvariable=cityvalue).grid(row=4, column=2)

Checkbutton(root, text="Want Coupon ? : ",
            variable=couponvalue).grid(row=5, column=2, pady=5)


Button(root, text="Submit Your Form", command=getvals).grid(
    row=6, column=2, pady=5)

root.mainloop()
