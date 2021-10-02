
from PyQt5 import QtCore, QtWidgets, QtGui


from controllers.BaseController import BaseController
from models.StandardItem import StandardItem


class OptionsWindowController(BaseController):
    def __init__(self, viewHandler, styleheetManager):
        super(OptionsWindowController, self).__init__(viewHandler)
        self.stylesheetManager = styleheetManager
        self.comboBox = None

    def setupUi(self, OptionsWindow):
        OptionsWindow.setObjectName("OptionsWindow")
        OptionsWindow.resize(400, 300)
        self.optionsTree = QtWidgets.QTreeView(OptionsWindow)
        self.optionsTree.setGeometry(QtCore.QRect(10, 10, 200, 100))
        self.optionsTree.setObjectName("optionsTree")
        self.optionsTree.setHeaderHidden(True)
        treeModel = QtGui.QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()
        Appearance = StandardItem('Appearance')
        Other = StandardItem('Other')
        rootNode.appendRow(Appearance)
        rootNode.appendRow(Other)
        self.optionsTree.setModel(treeModel)
        self.optionsTree.expandAll()
        self.optionsTree.doubleClicked.connect(lambda: self.item_doubleClicked(self.optionsTree.selectedIndexes()[0],OptionsWindow))
        self.pushButton = QtWidgets.QPushButton(OptionsWindow)
        self.pushButton.setGeometry(QtCore.QRect(310, 260, 81, 26))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(OptionsWindow)
        self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(lambda: self.changeStyleSheet())
        QtCore.QMetaObject.connectSlotsByName(OptionsWindow)

    def retranslateUi(self, OptionsWindow):
        _translate = QtCore.QCoreApplication.translate
        OptionsWindow.setWindowTitle(_translate("OptionsWindow", "Options"))
        self.pushButton.setText(_translate("OptionsWindow", "Apply"))
    def item_doubleClicked(self, index,OptionsWindow):
        if index.data() == 'Appearance':
            self.spawnEditWidget(OptionsWindow)
        else:
            if self.comboBox is not None:
                self.comboBox.deleteLater()
                self.comboBox = None


    def spawnEditWidget(self,OptionsWindow):
        if self.comboBox is None:
            self.comboBox = QtWidgets.QComboBox(OptionsWindow)
            self.comboBox.setGeometry(QtCore.QRect(230,12,150,25))
            self.comboBox.setObjectName("combobox")
            themes = self.stylesheetManager.getThemes()
            for i in themes:
                self.comboBox.addItem(i)
            self.comboBox.show()
            self.pushButton.setEnabled(True)
    def changeStyleSheet(self):
        self.stylesheetManager.setStyle(str(self.comboBox.currentText()))






