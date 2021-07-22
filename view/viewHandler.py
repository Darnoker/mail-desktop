from loginWindow import Ui_loginWindow
from PyQt5 import QtWidgets


class ViewHandler:
    def showLoginWindow(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        loginWindow = QtWidgets.QDialog()
        ui=Ui_loginWindow()
        ui.setupUi(loginWindow)
        loginWindow.show()
        sys.exit(app.exec_())
        




