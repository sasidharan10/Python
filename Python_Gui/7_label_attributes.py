from tkinter import *

root = Tk()

root.geometry("600x400")
root.minsize(400, 300)
root.maxsize(800, 600)

root.title("My Python GUI")

my_text = Label(text="Introduction to various styles of dance including Jazz, Funk, Hip Hop, Tap, \nBallet, Bollywood, Broadway and Contemporary Basic warm-up techniques, dance steps and combinations \nin small and large group settings Development of a deeper understanding of the roots of the various \ndance forms.", bg="black", fg="yellowgreen", font="calibri 12 italic", padx=20, pady=10, borderwidth=4,
                relief=GROOVE)

my_text.pack(anchor="sw", side=LEFT, fill=Y, padx=20, pady=20)


root.mainloop()

"""
*** Important Label Options ***

- text = adds text to label
- bd/backgroound = to modify background properties
- fg = to modify foreground properties
- font = sets the font
- padx = x padding
- pady = y padding
- relief = border styling - SUNKEN, RAISED, GROOVE, RIDGE

*** Important Pack Options ***

- anchor = nw,ne,sw,se
- side = TOP(by default), LEFT, BOTTOM, RIGHT
- fill = X,Y (to fill space in X-axis or Y-axis)
- padx = Padding x
- pady = Padding y


***Notes***

- anchor="sw" wont work unless you set side=BOTTOM
- fill Y will work only if side is set as LEFT or RIGHT
"""
