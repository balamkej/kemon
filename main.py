#!/usr/bin/env python

import tkinter as tk

root = tk.Tk()

height = 5
width = 5
for i in range(height): #Rows
    for j in range(width): #Columns
        b = tk.Entry(root, text="")
        b.grid(row=i, column=j)

tk.mainloop()