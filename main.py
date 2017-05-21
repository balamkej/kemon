#!/usr/bin/env python

# Here we provide the necessary imports.
# The basic GUI widgets are located in QtGui module. 
import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):

        exitAction = QAction('&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.setGeometry(100, 100, 600, 500)
        self.setWindowTitle('Kemon')
        self.setWindowIcon(QIcon('resources/icon.jpg'))        
    
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_()) 