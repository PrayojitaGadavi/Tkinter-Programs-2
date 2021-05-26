from tkinter import *
p = Tk()
p.geometry("400x300")

chkbtn1 = Checkbutton(p, text="hello")
chkbtn1.pack()

chkbtn2 = Checkbutton(p, text="tkinter")
chkbtn2.pack()

chkbtn3 = Checkbutton(p, text="python")
chkbtn3.pack()

p.mainloop()