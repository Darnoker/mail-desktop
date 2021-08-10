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
        self.loginService = None

    # function used to set up the login window
    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(409, 254)
        self.emailAdressLabel = QtWidgets.QLabel(loginWindow)
        self.emailAdressLabel.setGeometry(QtCore.QRect(10, 20, 47, 14))
        self.emailAdressLabel.setObjectName("emailAdressLabel")
        self.passwordLabel = QtWidgets.QLabel(loginWindow)
        self.passwordLabel.setGeometry(QtCore.QRect(10, 90, 51, 16))
        self.passwordLabel.setObjectName("passwordLabel")
        self.emailAdressField = QtWidgets.QLineEdit(loginWindow)
        self.emailAdressField.setGeometry(QtCore.QRect(90, 10, 161, 31))
        self.emailAdressField.setObjectName("emailAdressField")
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
        self.loginButton.clicked['bool'].connect(lambda: self.loginButtonAction())

    # function, that is used to name labels and window title.
    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "Login"))
        self.emailAdressLabel.setText(_translate("loginWindow", "Email:"))
        self.passwordLabel.setText(_translate("loginWindow", "Password:"))
        self.loginButton.setText(_translate("loginWindow", "Login"))

    def loginButtonAction(self):
        if self.checkFields():
            emailAccount = EmailAccount(self.emailAdressField.text(),
                                        self.passwordField.text())

            self.loginService = LoginService(emailAccount, self)
            self.emailService = EmailService(emailAccount)

            if self.loginService.login_():
                self.viewHandler.showMainWindow()
                self.viewHandler.closeLoginWindow()

    def checkFields(self):
        if not self.emailAdressField.text():
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
