from PyQt5.QtGui import QStandardItem, QColor, QFont

# Class, that defines standard item, used for tree view.
class StandardItem(QStandardItem):
    def __init__(self, txt=''):
        super(StandardItem, self).__init__()
        fnt = QFont('Open Sans')
        self.setEditable(False)
        self.setText(txt)

