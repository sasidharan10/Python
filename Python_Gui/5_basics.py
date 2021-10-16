import tkinter as tk

root=tk.Tk()
# inside we have to write our code for GUI

root.geometry("500x400") # (Width x Height)
root.minsize(300,300)    # max window size
root.maxsize(800,600)    # min window size
name=tk.Label(text="Welcome To GUI Tutorial")
name.pack()   # always remember to pack the label
root.mainloop()