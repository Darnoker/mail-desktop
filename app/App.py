import sys

from PyQt5 import QtWidgets
from view.ViewHandler import ViewHandler

class App:
    def __init__(self):
        self.core = QtWidgets.QApplication(sys.argv)
        self.viewHandler = ViewHandler()

    def run(self):
        self.viewHandler.showLoginWindow()
        sys.exit(self.core.exec_())


