#!/usr/bin/env python

import tkinter as tk
import numpy as np
from tkinter.font import Font
from PIL import ImageTk, Image

def buildGrid(h,w,f):
    height = h
    width = w
    for i in range(height): #Rows
        for j in range(width): #Columns
            b = tk.Spinbox(f, from_=0, to=1, width=1,
                           font=Font(family='Helvetica',
                           size=20,
                           weight='bold'))
            b.grid(row=i, column=j, padx=10, pady=10)

def gridArray(grid, height, width):
    children = [e.get() for e in grid.winfo_children()]
    gridArray = np.reshape(children, (height,width))
    return gridArray

class Application():

    def weave(self):
        return #Not Implemented
    
    def createWidgets(self):
        self.WARP = tk.Toplevel()
        self.WARP.title("Warp Grid")
        buildGrid(5,10,self.WARP)

        self.WEFT = tk.Toplevel()
        self.WEFT.title("Weft Grid")
        buildGrid(10,5,self.WEFT)

        self.TIEUP = tk.Toplevel()
        self.TIEUP.title("Tie-Up Grid")
        buildGrid(5,5,self.TIEUP)

        self.WEAVEBUTTON = tk.Button(self.root, text='Weave',
                                     command=self.weave)

        self.QUITBUTTON = tk.Button(self.root, text='Quit',
                                     command=self.root.quit)

        
        path = "resources/icon.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        self.PANEL = tk.Label(self.root, image=img)
        self.PANEL.image = img


        
        #print(gridArray(self.TIEUP,5,5))
        #print(gridArray(self.WARP,5,10))
        #print(gridArray(self.WEFT,10,5))
    
    
    def __init__(self, root): 
        
        self.root = root
        self.root.title("Kemon")
        self.root.geometry("150x150")

        self.createWidgets()

        #self.PANEL.pack(side="bottom", fill="both", expand="yes")
        self.PANEL.grid()
        self.WEAVEBUTTON.grid()
        self.QUITBUTTON.grid()
        
root = tk.Tk()
app = Application(root)
root.mainloop()
