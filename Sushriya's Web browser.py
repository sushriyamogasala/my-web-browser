import sys

import PyQt5

from PyQt5.QtWidgets import *

from PyQt5.QtWebEngineWidgets import *

from PyQt5.QtGui import *

from PyQt5.QtWidgets import *

from PyQt5.QtWebEngine import *

from PyQt5.QtWebEngineWidgets import *

from PyQt5.QtCore import *

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import *

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow




class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow,self).__init__()

        self.browser = QWebEngineView()
    
        self.browser.setUrl(QUrl('https://www.ecosia.org/'))
    
        self.setCentralWidget(self.browser)
    
        self.showMaximized()
    
        navbar = QToolBar()
        self.addToolBar(navbar)

        prevBtn = QAction('Previous',self)
        prevBtn.triggered.connect(self.browser.back)
        navbar.addAction(prevBtn)

        nextBtn = QAction('Next',self)
        nextBtn.triggered.connect(self.browser.forward)
        navbar.addAction(nextBtn)

        refreshBtn = QAction('Refresh',self)
        refreshBtn.triggered.connect(self.browser.reload)
        navbar.addAction(refreshBtn)

        homeBtn = QAction('Home',self)
        homeBtn.triggered.connect(self.home)
        navbar.addAction(homeBtn)
    
        self.searchBar = QLineEdit()
        self.searchBar.returnPressed.connect(self.loadUrl)
        navbar.addWidget(self.searchBar)
        self.browser.urlChanged.connect(self.updateUrl)

    def home(self):
        self.browser.setUrl(QUrl('https://www.ecosia.org/'))
    def loadUrl(self):
        url = self.searchBar.text()
        self.browser.setUrl(QUrl(url))
    def updateUrl(self, url):
        self.searchBar.setText(url.toString())

''' 
 if not Qurl:
        print("missing url")  

    else:
        print(url not available)
'''
MyApp = QApplication(sys.argv)
QApplication.setApplicationName("Sushriya's Web Browser")
window = MainWindow()

sys.exit(MyApp.exec_())