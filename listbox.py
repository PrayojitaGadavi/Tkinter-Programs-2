from tkinter import *

p = Tk()

lbox = Listbox(p)

lbox.insert(1, "list 1")
lbox.insert(2, "list 2")
lbox.insert(3, "list 3")

lbox.pack()

p.mainloop()