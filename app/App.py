# Main app class

import sys

from PyQt5 import QtWidgets
from view.ViewHandler import ViewHandler
from styles.StylesheetManager import StylesheetManager

class App:
    def __init__(self):
        self.core = QtWidgets.QApplication(sys.argv)
        self.StylesheetManager = StylesheetManager(self.core)
        self.viewHandler = ViewHandler(self.StylesheetManager)


    def run(self):
        self.StylesheetManager.setStyle(self.StylesheetManager.getThemes()[0])
        self.viewHandler.showLoginWindow()
        sys.exit(self.core.exec_())



