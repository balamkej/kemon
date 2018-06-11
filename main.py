#!/usr/bin/env python

import tkinter as tk
import numpy as np
import weaving as wv
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
    h = 5
    w = 10
    
    def weave(self):
        wv.weaving()
    
    def createWidgets(self):
        self.WARP = tk.Toplevel()
        self.WARP.title("Treadle Grid")
        buildGrid(self.h,self.w,self.WARP)

        self.THREADING = tk.Toplevel()
        self.THREADING.title("Threading Grid")
        buildGrid(self.w,self.h,self.THREADING)

        self.TIEUP = tk.Toplevel()
        self.TIEUP.title("Tie-Up Grid")
        buildGrid(self.h,self.h,self.TIEUP)

        self.WEAVEBUTTON = tk.Button(self.root, text='Weave',
                                     command=self.weave)

        self.QUITBUTTON = tk.Button(self.root, text='Quit',
                                     command=self.root.quit)

        
        path = "resources/icon.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        self.PANEL = tk.Label(self.root, image=img)
        self.PANEL.image = img


        
        #print(gridArray(self.TIEUP,5,5))
        #print(gridArray(self.TREADLE,5,10))
        #print(gridArray(self.THREADING,10,5))
    
    
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
