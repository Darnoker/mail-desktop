from controllers.MainWindowController import MainWindowController
from controllers.LoginWindowController import LoginWindowController
from PyQt5 import QtWidgets


# ViewHandler is a class, that performs view-related actions, for example: showing login window
# and closing it.

class ViewHandler:
    def __init__(self):
        self.loginWindow = QtWidgets.QDialog()
        self.mainWindow = QtWidgets.QMainWindow()
        self.loginWindowController = LoginWindowController(self)
        self.mainWindowController = MainWindowController(self)
        self.loginWindowController.setupUi(self.loginWindow)
        self.mainWindowController.setupUi(self.mainWindow)
        self.emailService = None

    def showLoginWindow(self):
        self.loginWindow.show()

    def showMainWindow(self):
        self.mainWindow.show()

    def closeLoginWindow(self):
        self.loginWindow.close()
