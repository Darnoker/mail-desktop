# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets

# LoginWindowController is a class, that describes our login window and all logic behind it.
from controllers.BaseController import BaseController
from models.EmailAccount import EmailAccount
from services.EmailService import EmailService
from services.LoginService import LoginService


class LoginWindowController(BaseController):
    def __init__(self, viewHandler):
        super(LoginWindowController, self).__init__(viewHandler)

    # function used to set up the login window
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(409, 254)
        self.emailAddressLabel = QtWidgets.QLabel(loginWindow)
        self.emailAddressLabel.setGeometry(QtCore.QRect(10, 20, 47, 14))
        self.emailAddressLabel.setObjectName("emailAddressLabel")
        self.passwordLabel = QtWidgets.QLabel(loginWindow)
        self.passwordLabel.setGeometry(QtCore.QRect(10, 90, 51, 16))
        self.passwordLabel.setObjectName("passwordLabel")
        self.emailAddressField = QtWidgets.QLineEdit(loginWindow)
        self.emailAddressField.setGeometry(QtCore.QRect(90, 10, 161, 31))
        self.emailAddressField.setObjectName("emailAddressField")
        self.passwordField = QtWidgets.QLineEdit(loginWindow)
        self.passwordField.setGeometry(QtCore.QRect(90, 80, 161, 31))
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordField.setObjectName("passwordField")
        self.loginButton = QtWidgets.QPushButton(loginWindow)
        self.loginButton.setGeometry(QtCore.QRect(170, 130, 91, 31))
        self.loginButton.setObjectName("loginButton")
        self.errorLabel = QtWidgets.QLabel(loginWindow)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setGeometry(QtCore.QRect(10, 190, 261, 16))
        self.retranslateUi(loginWindow)
        self.loginButton.clicked['bool'].connect(lambda: self.createLoginThread())

    # function, that is used to name labels and window title.
    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "Login"))
        self.emailAddressLabel.setText(_translate("loginWindow", "Email:"))
        self.passwordLabel.setText(_translate("loginWindow", "Password:"))
        self.loginButton.setText(_translate("loginWindow", "Login"))

    def createLoginThread(self):
        emailAccount = EmailAccount(self.emailAddressField.text(),
                                    self.passwordField.text())

        self.viewHandler.emailService = EmailService(emailAccount)
        self.workerThread = LoginService(emailAccount, self, self.viewHandler)
        self.workerThread.started.connect(lambda : self.loginButton.setEnabled(False))
        self.workerThread.finished.connect(lambda: self.loginButton.setEnabled(True))
        self.workerThread.finished.connect(lambda: self.openMainWindow(self.workerThread.FLAG))
        self.workerThread.start()

    def openMainWindow(self, flag):
        if flag:
            self.viewHandler.initMailTreeView()
            self.viewHandler.showMainWindow()
            self.viewHandler.closeLoginWindow()

    # checks if fields for email address and password aren't empty.
    def checkFields(self):
        if not self.emailAddressField.text():
            self.errorLabel.setText("Email Address field is empty!")
            return False

        if not self.passwordField.text():
            self.errorLabel.setText("Password field is empty!")
            return False

        return True

# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     loginWindow = QtWidgets.QDialog()
#     ui = Ui_loginWindow()
#     ui.setupUi(loginWindow)
#     loginWindow.show()
#     sys.exit(app.exec_())
