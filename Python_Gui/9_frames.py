from tkinter import *

root=Tk()
root.title("Python GUI")
root.geometry("600x400")
f1=Frame(root,bg="grey",borderwidth=4)
f1.pack(fill=X)

l1=Label(f1,text="Welcome to Python GUI",font="Arial 15 bold")
l1.pack(fill=X,padx=2,pady=2)

f2=Frame(root,borderwidth=3,bg="black")
f2.pack(pady=20)
l2=Label(f2,text="Introduction to various styles of dance including Jazz, Funk, Hip Hop, Tap, \nBallet, Bollywood, Broadway and Contemporary Basic warm-up techniques, dance steps and combinations \nin small and large group settings Development of a deeper understanding of the roots of the various \ndance forms.",font="calibri 10 italic",pady=20,padx=10)
l2.pack()

root.mainloop()