# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\loginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginWindow(object):
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
        self.passwordField.setObjectName("passwordField")
        self.loginButton = QtWidgets.QPushButton(loginWindow)
        self.loginButton.setGeometry(QtCore.QRect(170, 130, 91, 31))
        self.loginButton.setObjectName("loginButton")

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "Login"))
        self.emailAdressLabel.setText(_translate("loginWindow", "Email:"))
        self.passwordLabel.setText(_translate("loginWindow", "Password:"))
        self.loginButton.setText(_translate("loginWindow", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginWindow = QtWidgets.QDialog()
    ui = Ui_loginWindow()
    ui.setupUi(loginWindow)
    loginWindow.show()
    sys.exit(app.exec_())