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
