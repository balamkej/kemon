#!/usr/bin/env python

import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Kemon")
root.geometry("100x100")

path = "resources/icon.jpg"
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")


# Warp Grid

warp = tk.Toplevel()
warp.title("Warp Grid")

height = 5
width = 5
for i in range(height): #Rows
    for j in range(width): #Columns
        b = tk.Spinbox(warp, from_=0, to=1, width=1,
                       font=Font(family='Helvetica',
                       size=20,
                       weight='bold'))
        b.grid(row=i, column=j, padx=10, pady=10)


# Weft Grid

# Tie-up

# Color Palette

# Menu


root.mainloop()


#from tkinter.colorchooser import *
#def getColor():
#    color = askcolor() 
#    print color
#Button(text='Select Color', command=getColor).pack()
