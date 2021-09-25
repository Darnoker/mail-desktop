# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QAbstractItemView
from services.FetchHeadersService import FetchHeadersService

from models.StandardItem import StandardItem

# MainWindowController is a class, that describes main window and all logic behind it.


from controllers.BaseController import BaseController
from services.FetchMessagesService import FetchMessagesService


class MainWindowController(BaseController):
    def __init__(self, viewHandler, emailManager):
        super(MainWindowController, self).__init__(viewHandler, emailManager)

    # function, that is called to set up the main window.
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(708, 627)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setObjectName("treeView")
        self.horizontalLayout.addWidget(self.treeView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.verticalHeader().setHidden(True)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(213, 206))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 708, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.treeView.setIndentation(12)
        self.treeView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.treeView.pressed.connect(lambda: self.getHeaders())
        self.tableWidget.pressed.connect(lambda: self.getMessage())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Sender"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Subject"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))

    def initTreeView(self):
        self.treeView.setModel(self.emailManager.treeModel)
        self.treeView.setRootIndex(self.emailManager.root.index())
        self.treeView.setHeaderHidden(True)
        self.treeView.setExpanded(self.emailManager.treeItem.index(), True)
        for i in range(self.emailManager.treeItem.rowCount()):
            self.treeView.setExpanded(self.emailManager.treeItem.child(i, 0).index(), True)

    def getHeaders(self):
        try:
            index = self.treeView.selectedIndexes()[0]
            index_ = index
            parent = "None"
            while index_.parent().data() is not None:
                parent = index_.parent().data()
                index_ = index_.parent()
            folderName = index.data()
            emailAccount = self.emailManager.accountDict[parent]
            self.fetchHeadersService = FetchHeadersService(emailAccount, folderName, self.emailManager)
            self.fetchHeadersService.finished.connect(lambda: self.showHeaders())
            self.fetchHeadersService.start()
        except Exception as e:
            print(str(e))

    def showHeaders(self):
        senderList = self.fetchHeadersService.senderList
        senderList.reverse()
        emailList = self.fetchHeadersService.emailList
        emailList.reverse()
        subjectList = self.fetchHeadersService.subjectList
        subjectList.reverse()
        messageNumber = self.fetchHeadersService.messageNumber
        columnCount = self.tableWidget.columnCount()
        self.tableWidget.setRowCount(messageNumber)

        for i in range(columnCount):
            for j in range(messageNumber):
                if i == 0:
                    sender_ = QtWidgets.QTableWidgetItem(senderList[j])
                    self.tableWidget.setItem(j, i, sender_)
                if i == 1:
                    email_ = QtWidgets.QTableWidgetItem(emailList[j])
                    self.tableWidget.setItem(j, i, email_)
                if i == 2:
                    subject_ = QtWidgets.QTableWidgetItem(subjectList[j])
                    self.tableWidget.setItem(j, i, subject_)

    def getMessage(self):
        row = self.tableWidget.currentRow() + 1
        emailAccount = self.fetchHeadersService.emailAccount
        messageID = self.fetchHeadersService.idDict[row]
        self.fetchMessagesService = FetchMessagesService(emailAccount, messageID)
        self.fetchMessagesService.finished.connect(lambda: self.showMessage())
        self.fetchMessagesService.start()

    def showMessage(self):
        message = self.fetchMessagesService.message
        self.textBrowser.setText(message)

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())