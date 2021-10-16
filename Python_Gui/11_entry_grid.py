from tkinter import *

def details():
    print(f"Username is : {uservalue.get()}")
    print(f"Pssword is : {passvalue.get()}")

root = Tk()
root.geometry("600x400")
root.title("User Login")

user = Label(root, text="Username : ")
user.grid()
password = Label(root, text="Password : ")
password.grid()

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
userentry.grid(row=0, column=1)
passentry = Entry(root, textvariable=passvalue)
passentry.grid(row=1, column=1)

btn = Button(root, text="Submit", command=details)
btn.grid(row=2)

root.mainloop()

"""
***** Variable classes in tkinter *****

- BooleanVar
- IntVar
- DoubleVar
- StringVar

"""
