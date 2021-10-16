import tkinter as tk
from PIL import Image,ImageTk

root=tk.Tk()

root.geometry("600x400")
root.minsize(400,300)

# photo=tk.PhotoImage(file="logo.png") # for png files

img=Image.open("pic.jpg")              # for jpg files
photo=ImageTk.PhotoImage(img)
tk.Label(image=photo).pack()
root.mainloop()

"""
- Tkinter only supports 'png' files and does not support 'jpeg' files
- use PIL to use jpeg files
"""