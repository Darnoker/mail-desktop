from PyQt5 import QtCore, QtWidgets


from controllers.BaseController import BaseController

class OptionsWindowController(BaseController):
    def __init__(self, viewHandler):
        super(OptionsWindowController, self).__init__(viewHandler)

    def setupUi(self, OptionsWindow):
        OptionsWindow.setObjectName("OptionsWindow")
        OptionsWindow.resize(400, 300)
        self.view = QtWidgets.QPushButton(OptionsWindow)
        self.view.setGeometry(QtCore.QRect(10, 10, 81, 26))
        self.view.setObjectName("viewButton")
        self.pushButton = QtWidgets.QPushButton(OptionsWindow)
        self.pushButton.setGeometry(QtCore.QRect(310, 260, 81, 26))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(OptionsWindow)
        #self.pushButton.clicked.connect(lambda: self.spawnWidget())
        QtCore.QMetaObject.connectSlotsByName(OptionsWindow)

    def retranslateUi(self, OptionsWindow):
        _translate = QtCore.QCoreApplication.translate
        OptionsWindow.setWindowTitle(_translate("OptionsWindow", "Options"))
        self.view.setText(_translate("OptionsWindow", "Edit"))
        self.pushButton.setText(_translate("OptionsWindow", "Apply"))






