from view.mainWindow import Ui_MainWindow
from view.loginWindow import Ui_loginWindow
from PyQt5 import QtWidgets
import sys


class ViewHandler:
    def showLoginWindow(self):
        app = QtWidgets.QApplication(sys.argv)
        loginWindow = QtWidgets.QDialog()
        ui = Ui_loginWindow()
        ui.setupUi(loginWindow)
        loginWindow.show()
        sys.exit(app.exec_())
    
    def showMainWindow(self):
        app = QtWidgets.QApplication(sys.argv)
        mainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(mainWindow)
        mainWindow.show()
        sys.exit(app.exec_())
