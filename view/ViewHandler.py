from controllers.MainWindowController import MainWindowController
from controllers.LoginWindowController import LoginWindowController
from PyQt5 import QtWidgets


# ViewHandler is a class, that performs view related actions, for example: showing login window
# and closing it.
from services.EmailManager import EmailManager


class ViewHandler:
    def __init__(self):
        self.emailManager = EmailManager(self)

    def showLoginWindow(self):
        self.loginWindow = QtWidgets.QDialog()
        self.loginWindowController = LoginWindowController(self, self.emailManager)
        self.loginWindowController.setupUi(self.loginWindow)
        self.loginWindow.show()

    def showMainWindow(self):
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindowController = MainWindowController(self, self.emailManager)
        self.mainWindowController.setupUi(self.mainWindow)
        self.mainWindow.show()

    def closeLoginWindow(self):
        self.loginWindow.close()

    def initMailTreeView(self):
        self.mainWindowController.initTreeView()
