#!/usr/bin/env python

import tkinter as tk
from tkinter.font import Font

root = tk.Tk()

height = 5
width = 5
for i in range(height): #Rows
    for j in range(width): #Columns
        b = tk.Spinbox(root, from_=0, to=1, width=1,
                       font=Font(family='Helvetica',
                       size=20,
                       weight='bold'))
        b.grid(row=i, column=j, padx=10, pady=10)

tk.mainloop()



# Warp Grid

# Weft Grid

# Tie-up

# Color Palette

# Menu





#from tkinter.colorchooser import *
#def getColor():
#    color = askcolor() 
#    print color
#Button(text='Select Color', command=getColor).pack()
