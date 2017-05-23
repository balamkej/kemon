#!/usr/bin/env python

# Here we provide the necessary imports.
# The basic GUI widgets are located in QtGui module. 
import sys
from PyQt5.QtWidgets import (QWidget, QMainWindow, QAction, qApp, QApplication, QPushButton)
from PyQt5.QtGui import QIcon
import mwDesign

# The MainWindow class inherits from the QMainWindow class
class KemonApp(QMainWindow, mwDesign.Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(KemonApp,self).__init__()
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    mw = KemonApp()
    mw.show()
    app.exec_()

if __name__ == '__main__':
    main()