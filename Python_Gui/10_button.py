from tkinter import *

def adding():
    print("5 + 3 =",(5+3))

def subtracting():
    print("5 - 3 =",(5-3))

root=Tk()
root.geometry("600x400")
root.title("Calculator")

f1 = Frame(root)
f1.pack(anchor=NW)
b1=Button(f1,text="Add",background="light grey",borderwidth=3,command=adding)
b1.pack(side=LEFT,padx=3,pady=3)
b2=Button(f1,text="Sub",background="light grey",borderwidth=3,command=subtracting)
b2.pack(side=LEFT,padx=3,pady=3)



root.mainloop()