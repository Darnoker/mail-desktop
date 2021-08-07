from view.windows.MainWindow import Ui_MainWindow
from view.windows.LoginWindow import Ui_loginWindow
from PyQt5 import QtWidgets

# ViewHandler is a class, that performs view-related actions, for example: showing login window
# and closing it.

class ViewHandler:
    def __init__(self):
        self.loginWindow = QtWidgets.QDialog()
        self.mainWindow = QtWidgets.QMainWindow()
        self.ui_LoginWindow = Ui_loginWindow(self)
        self.ui_MainWindow = Ui_MainWindow()
        self.ui_LoginWindow.setupUi(self.loginWindow)
        self.ui_MainWindow.setupUi(self.mainWindow)

    def showLoginWindow(self):
        self.loginWindow.show()

    def showMainWindow(self):
        self.mainWindow.show()

    def closeLoginWindow(self):
        self.loginWindow.close()
