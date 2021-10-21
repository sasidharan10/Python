from tkinter import *

def showdata(event):
    print(f"User clicked the {event.x}, {event.y} button!!!")

root=Tk()
root.geometry("600x400")
root.title("Event in tkinter")

btn=Button(root,text="Click here")
btn.pack()
btn.bind('<Button-1>', showdata)
btn.bind('<Double-1>', quit)

root.mainloop()