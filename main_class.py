#!/usr/bin/env python

import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image

class Application():

#    def say_hi(self):
#        print("hi there, everyone!")
#
#    def createWidgets(self):
#        self.QUIT = tk.Button(self)
#        self.QUIT["text"] = "QUIT"
#        self.QUIT["fg"]   = "red"
#        self.QUIT["command"] =  self.quit
#
#        self.QUIT.pack({"side": "left"})
#
#        self.hi_there = tk.Button(self)
#        self.hi_there["text"] = "Hello",
#        self.hi_there["command"] = self.say_hi
#
#        self.hi_there.pack({"side": "left"})
#

    def __init__(self, root, title): 

        
        self.root = root
        self.root.title(title)
        self.root.geometry("150x150")
        
        path = "resources/icon.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        
        self.PANEL = tk.Label(self.root, image=img)
        self.PANEL.image = img
        self.PANEL.pack(side="bottom", fill="both", expand="yes")
        #self.createWidgets()
        
root = tk.Tk()
app = Application(root, 'Kemon')
root.mainloop()
