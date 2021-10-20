from tkinter import *

root= Tk()
root.geometry("600x400")
root.title("Geometry")

wid=Canvas(root,width=600,height=400)
wid.pack()

# from x1,y1 to x2,y2
wid.create_line(0,400,600,0,fill="violet")

wid.create_rectangle(100,100,300,200,fill="light grey")

wid.create_oval(50,50,100,100,fill="limegreen")

wid.create_text(60,20,text="Hello World",fill="Blue",font="calibri 12 bold")






root.mainloop()