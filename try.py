
from tkinter import *

root = Tk()
root.config(padx=20, pady=20)

b1 = Button(root, text='b1')
b2 = Button(root, text='b2')
ip = Entry(width=5)
b1.grid(column=0, row=0)   # grid dynamically divides the space in a grid
b2.grid(column=1, row=0)
ip.grid(column=2, row=0)# and arranges widgets accordingly
root.mainloop()