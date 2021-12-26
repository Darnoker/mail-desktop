from controllers.MainWindowController import MainWindowController
from controllers.LoginWindowController import LoginWindowController
from controllers.OptionsWindowController import OptionsWindowController
from PyQt5 import QtWidgets


# ViewHandler is a class, that performs view related actions, for example: showing login window
# and closing it.
from controllers.SendWindowController import SendWindowController
from services.EmailManager import EmailManager

# Class that manages view flow (maybe should be renamed to ViewManager?)
class ViewHandler:
    def __init__(self,stylesheetManager):
        self.emailManager = EmailManager(self)
        self.stylesheetManager = stylesheetManager

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

    def showOptionsWindow(self):
        self.optionsWindow= QtWidgets.QWidget()
        self.optionWindowController = OptionsWindowController(self,self.stylesheetManager)
        self.optionWindowController.setupUi(self.optionsWindow)
        self.optionsWindow.show()

    def showSendWindow(self):
        self.sendWindow = QtWidgets.QDialog()
        self.sendWindowController = SendWindowController(self, self.emailManager)
        self.sendWindowController.setupUi(self.sendWindow)
        self.sendWindow.show()

