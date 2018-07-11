#!/usr/bin/env python

import tkinter as tk
import numpy as np
import weaving as wv
import matplotlib.pyplot as plt
import matplotlib.cm as cm
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
    gridArray = gridArray.astype(np.float)
    return gridArray

class Application():
    h = 4
    w = 10
    
    def weave(self):
        th_grid = gridArray(self.THREADING,self.h,self.w)
        tr_grid = gridArray(self.TREADLE,self.w,self.h)
        ti_grid = gridArray(self.TIEUP,self.h,self.h)
        weav_img = wv.weave(tr_grid,th_grid,ti_grid)
        plt.imsave('temp/' + 'test.png', weav_img, cmap=cm.gray)

    def makeLoom(self):
        th_h = self.TH_HEIGHTSCALE.get()
        th_w = self.TH_WIDTHSCALE.get()
        tr_h = self.TR_HEIGHTSCALE.get()        

        self.THREADING = tk.Toplevel()
        self.THREADING.title("Threading Grid")
        buildGrid(th_h,th_w,self.THREADING)

        self.TREADLE = tk.Toplevel()
        self.TREADLE.title("Treadle Grid")
        buildGrid(tr_h,th_h,self.TREADLE)

        self.TIEUP = tk.Toplevel()
        self.TIEUP.title("Tie-Up Grid")
        buildGrid(th_h,th_h,self.TIEUP)

    
    def createWidgets(self):
        self.TH_WIDTHSCALE = tk.Scale(self.root, from_=0, to=100, label="Threading Width", orient=tk.HORIZONTAL)
        self.TH_HEIGHTSCALE = tk.Scale(self.root, from_=0, to=100, label="Threading Height", orient=tk.HORIZONTAL)
        self.TR_HEIGHTSCALE = tk.Scale(self.root, from_=0, to=100, label="Treadle Height", orient=tk.HORIZONTAL)
        self.TILEHEIGHT = tk.Scale(self.root, from_=0, to=100, label="Tile Height x Times", orient=tk.HORIZONTAL)
        self.TILEWIDTH = tk.Scale(self.root, from_=0, to=100, label="Tile Width x Times", orient=tk.HORIZONTAL)

        self.GRIDBUTTON = tk.Button(self.root, text='Set-up Loom',
                                     command=self.makeLoom)

        self.WEAVEBUTTON = tk.Button(self.root, text='Weave',
                                     command=self.weave)

        self.QUITBUTTON = tk.Button(self.root, text='Quit',
                                     command=self.root.quit)

        
        path = "resources/icon.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        self.PANEL = tk.Label(self.root, image=img)
        self.PANEL.image = img
    
    
    def __init__(self, root): 
        
        self.root = root
        self.root.title("Kemon")
        self.root.geometry("500x500")

        self.createWidgets()

        self.PANEL.grid()
        self.WEAVEBUTTON.grid()
        self.GRIDBUTTON.grid()
        self.QUITBUTTON.grid()
        self.TH_WIDTHSCALE.grid()
        self.TH_HEIGHTSCALE.grid()
        self.TR_HEIGHTSCALE.grid()
        self.TILEWIDTH.grid()
        self.TILEHEIGHT.grid()

root = tk.Tk()
app = Application(root)
root.mainloop()
