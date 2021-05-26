from tkinter import *
p = Tk()

txt = Text(p, height=3, width = 35)
txt.pack()

txt.insert(END, 'Welcome to World of Tkinter')

p.mainloop()