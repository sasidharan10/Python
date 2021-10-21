from tkinter import *

root=Tk()
root.geometry("600x500")
root.title("Multiple Pages")

def tab1():
    def tab2():
        def back():
            l2.destroy()
            b2.destroy()
            tab1()
        l2=Label(text="***** Second page *****",font="calibri 20 bold")
        l2.pack()
        b2=Button(text="First",font="arial 12",command=back)
        b2.pack()

        l1.destroy()
        b1.destroy()
        
    l1=Label(text="***** First page *****",font="calibri 20 bold")
    l1.pack()
    b1=Button(text="Second",font="arial 12",command=tab2)
    b1.pack()
    
        

tab1()
root.mainloop()