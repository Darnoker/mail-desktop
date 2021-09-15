# -*- coding: utf-8 -*-

# Class, used to manage email actions.
import email

from PyQt5 import QtGui

from models.StandardItem import StandardItem
from email.header import decode_header

from services.FetchFoldersService import FetchFoldersService
from services.FetchHeadersService import FetchHeadersService




class EmailManager:
    def __init__(self, viewHandler):
        self.viewHandler = viewHandler
        self.folderDict = {}
        self.accountDict = {}

    def addEmailAccount(self, emailAccount):
        self.treeModel = QtGui.QStandardItemModel()
        self.root = self.treeModel.invisibleRootItem()
        self.foldersList = []
        self.folderDict = {}
        self.treeItem = StandardItem(emailAccount.address)
        self.treeItem.setSelectable(False)
        self.fetchFoldersService = FetchFoldersService(self.treeItem, emailAccount, self)
        self.fetchFoldersService.finished.connect(lambda: self.root.appendRow(self.treeItem))
        self.fetchFoldersService.finished.connect(lambda: self.openMainWindow())
        self.fetchFoldersService.start()

    def getEmailHeaders(self, emailAccount, folderName):
        self.fetchHeadersService = FetchHeadersService(emailAccount, folderName, self)
        self.fetchHeadersService.started.connect(lambda: print("START"))
        self.fetchHeadersService.start()

    def openMainWindow(self):
        self.viewHandler.showMainWindow()
        self.viewHandler.initMailTreeView()
        self.viewHandler.closeLoginWindow()
