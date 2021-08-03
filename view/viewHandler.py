from view.mainWindow import Ui_MainWindow
from view.loginWindow import Ui_loginWindow
from PyQt5 import QtWidgets



class ViewHandler:
    def __init__(self):
        self.loginWindow = QtWidgets.QDialog()
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui_LoginWindow = Ui_loginWindow()
        self.ui_MainWindow = Ui_MainWindow()

    def showLoginWindow(self):
        self.ui_LoginWindow.setupUi(self.loginWindow)
        self.loginWindow.show()


    def showMainWindow(self):
        self.ui_MainWindow.setupUi(self.mainWindow)
        self.mainWindow.show()
