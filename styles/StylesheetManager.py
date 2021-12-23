from os import listdir
from pathlib import Path
from PyQt5 import QtWidgets

# Class that manages styles
class StylesheetManager:
    def __init__(self, app: QtWidgets.QApplication):
        self.app = app
        self.stylesheet = None
        self.themeList = [Path(f).stem for f in listdir(Path(__file__).parent / 'resources') if f.endswith('.qss')] # checking extension of file in dir

    # getting theme list
    def getThemes(self):
        return self.themeList

    # setting up style
    def setStyle(self, theme):
        path = Path(__file__).parent / 'resources' / str(theme+'.qss')
        self.stylesheet = Path(path).read_text()
        self.app.setStyleSheet(self.stylesheet)