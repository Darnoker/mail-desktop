from controllers.MainWindowController import MainWindowController
from controllers.LoginWindowController import LoginWindowController
from PyQt5 import QtWidgets


# ViewHandler is a class, that performs view-related actions, for example: showing login window
# and closing it.

class ViewHandler:
    def __init__(self):
        self.loginWindow = QtWidgets.QDialog()
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui_LoginWindow = LoginWindowController(self)
        self.ui_MainWindow = MainWindowController(self)
        self.ui_LoginWindow.setupUi(self.loginWindow)
        self.ui_MainWindow.setupUi(self.mainWindow)

    def showLoginWindow(self):
        self.loginWindow.show()

    def showMainWindow(self):
        self.mainWindow.show()

    def closeLoginWindow(self):
        self.loginWindow.close()
