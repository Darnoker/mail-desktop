# -*- coding: utf-8 -*-

# Class, used to manage email actions.
import email

from PyQt5 import QtGui

from models.StandardItem import StandardItem
from email.header import decode_header

from services.FetchFoldersService import FetchFoldersService





# def decode(string_):
#     full_string = ""
#     for i in range(len(string_)):
#         if isinstance(string_[i][0], bytes):
#             decoded_string = string_[i][0].decode('utf-8')
#             full_string += decoded_string
#         else:
#             full_string += string_[i][0]
#
#     return full_string


class EmailManager:
    def __init__(self, viewHandler):
        self.viewHandler = viewHandler

    def addEmailAccount(self, emailAccount):
        self.treeModel = QtGui.QStandardItemModel()
        self.root = self.treeModel.invisibleRootItem()
        self.foldersList = []
        self.folderDict = {}
        self.treeItem = StandardItem(emailAccount.address)
        print(self.treeItem.whatsThis())
        self.treeItem.setSelectable(False)
        self.fetchFoldersService = FetchFoldersService(self.treeItem, emailAccount)
        self.fetchFoldersService.finished.connect(lambda: self.root.appendRow(self.treeItem))
        self.fetchFoldersService.finished.connect(lambda: self.openMainWindow())
        self.fetchFoldersService.finished.connect(lambda: print(self.fetchFoldersService.folderDict))
        self.fetchFoldersService.start()

    def getEmailHeaders(self, emailAccount):
        pass

    def openMainWindow(self):
        self.viewHandler.showMainWindow()
        self.viewHandler.initMailTreeView()
        self.viewHandler.closeLoginWindow()



    # def showMessages(self, folder):
    #     self.emailAccount.mail.select_folder(folder, readonly=True)
    #     messages = self.emailAccount.mail.search("ALL")
    #     for message_id, message_data in self.emailAccount.mail.fetch(messages, ['RFC822']).items():
    #         email_message = email.message_from_bytes(message_data[b'RFC822'])
    #         if email_message.is_multipart():
    #             # decoding sender and subject
    #             from_ = email_message.get("From")
    #             from_ = decode_header(from_)
    #             subject_ = email_message.get("Subject")
    #             subject_ = decode_header(subject_)
    #             full_sender = decode(from_)
    #             full_subject = decode(subject_)
    #             print(message_id, "FROM:", full_sender, " SUBJECT:", full_subject)
