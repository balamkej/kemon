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

    def weave(self):
        th_h = int(self.TH_HEIGHTSCALE.get())
        th_w = int(self.TH_WIDTHSCALE.get())
        tr_h = int(self.TR_HEIGHTSCALE.get())        

        th_grid = gridArray(self.THREADING,th_h,th_w)
        tr_grid = gridArray(self.TREADLE,tr_h,th_h)
        ti_grid = gridArray(self.TIEUP,th_h,th_h)
        weav_img = wv.weave(tr_grid,th_grid,ti_grid)
        weav_img = np.tile(weav_img, (100,100))
        plt.imsave('temp/' + 'test.png', weav_img, cmap=cm.gray)

    def makeLoom(self):
        th_h = int(self.TH_HEIGHTSCALE.get())
        th_w = int(self.TH_WIDTHSCALE.get())
        tr_h = int(self.TR_HEIGHTSCALE.get())        

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
        self.TH_WIDTHSCALE = tk.Spinbox(self.root, from_=1, to=100, width=4,
                           font=Font(family='Helvetica',
                           size=20,
                           weight='bold'))
        tk.Label(self.TH_WIDTHSCALE, text="Threading Width") 

        self.TH_HEIGHTSCALE = tk.Spinbox(self.root, from_=1, to=100, width=4,
                           font=Font(family='Helvetica',
                           size=20,
                           weight='bold'))
        tk.Label(self.TH_HEIGHTSCALE, text="Threading Height") 

        self.TR_HEIGHTSCALE = tk.Spinbox(self.root, from_=1, to=100, width=4,
                           font=Font(family='Helvetica',
                           size=20,
                           weight='bold'))
        tk.Label(self.TR_HEIGHTSCALE, text="Treadle Height")

        self.TILEHEIGHT = tk.Spinbox(self.root, from_=1, to=100, width=4,
                           font=Font(family='Helvetica',
                           size=20,
                           weight='bold'))
        tk.Label(self.TILEHEIGHT, text="Tile Height X Times")

        self.TILEWIDTH = tk.Spinbox(self.root, from_=1, to=100, width=4,
                           font=Font(family='Helvetica',
                           size=20,
                           weight='bold'))
        tk.Label(self.TILEWIDTH, text="Tile Width X Times")

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
